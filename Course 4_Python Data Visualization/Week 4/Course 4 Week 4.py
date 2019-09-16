"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    table = {}
    with open(codeinfo["codefile"], newline = '') as csvfile:
        csvreader = csv.DictReader(csvfile, \
                                   delimiter = codeinfo["separator"], \
                                   quotechar = codeinfo["quote"])
        for row in csvreader:
            rowid = row[codeinfo["plot_codes"]]
            table[rowid] = row[codeinfo["data_codes"]]           
    return table


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    code_dict = {}
    code_not_found = set()
    code_table = build_country_code_converter(codeinfo)  #{A:AA}
    for codes1 in plot_countries:  #a
        codes3 = ''
        dummy1 = 0
        
        for codes2 in code_table:
            if codes1.lower() == codes2.lower():
                codes3 = code_table[codes2]
                break
            else:
                dummy1 += 1
        if dummy1 == len(code_table):
            code_not_found.add(codes1)
            
        dummy2 = 0
        for codes4 in gdp_countries:  #AA
            if codes3.lower() == codes4.lower():
                code_dict[codes1] = codes4
                break
            else:
                dummy2 += 1
        if dummy2 == len(gdp_countries):
            code_not_found.add(codes1)
            #{'eh', 'gf', 'tw', 'sh', 'aq', 'yt', 're', 'va'}
            
    return code_dict, code_not_found


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    table = {}
    with open(gdpinfo["gdpfile"], newline = '') as csvfile:
        csvreader = csv.DictReader(csvfile, \
                                   delimiter = gdpinfo["separator"], \
                                   quotechar = gdpinfo["quote"])
        for row in csvreader:
            rowid = row[gdpinfo["country_code"]]
            table[rowid] = row.get(year)

    code_dict, code_not_found = reconcile_countries_by_code(codeinfo, plot_countries, table)
    code_to_gdp = {}
    no_gdp = set()
    for codes in code_dict:  #a
        if (table[code_dict[codes]] == '') or (table[code_dict[codes]] is None):
            no_gdp.add(codes)
        else:
            stat = float(table[code_dict[codes]])
            code_to_gdp[codes] = math.log10(stat)
    return code_to_gdp, code_not_found, no_gdp


def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    worldmap_gdp = pygal.maps.world.World()
    title = 'GDP by country for {0} (log scale), unified by common country NAME'
    worldmap_gdp.title = title.format(year)
    code_to_gdp, code_not_found, no_gdp = \
                 build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
    
    worldmap_gdp.add('GDP for {0}'.format(year), code_to_gdp)
    worldmap_gdp.add('Missing from World Bank Data', code_not_found)
    worldmap_gdp.add('No GDP data', no_gdp)
    
    worldmap_gdp.render_to_file(map_file)


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

#test_render_world_map()