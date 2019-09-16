"""
Dexter Wei: Test
Dexter Wei: changed language to python
Dexter Wei: Good morning. I am Zhengxiao (Dexter) Wei.
Dexter Wei: renamed document to None
Ke Shao: Hey Dexter, are you there?
Dexter Wei: Yes, I am.
Ke Shao: Hi, This is Ke, software engineer from Fresh Digital Group, how are you?
Dexter Wei: Hello, Ke. I am doing great. Thank you for having me here.
Ke Shao: Since the snow storm, I'm not at the office right now, so let's keep this technical interview short and tight, ok?
Dexter Wei: Sure. Take good care.
Ke Shao: I'll copy paste a question for you. It will takes roughly 15 mins to finish. After that, maybe you could ask me some questions about the company.
Dexter Wei: OK. I am ready.
Ke Shao: Baiscally, I want you to write a function to solve this problem
Ke Shao: take the input as the root node of a binary tree, and return a integer as the maximum depth
Dexter Wei: Understood.
Dexter Wei: Am I using Python programming language?
Ke Shao: yeah, sure. use whatever language you like
Dexter Wei: OK.
Dexter Wei: I am finished.
Ke Shao: Great!
Ke Shao: Looks good to me
Ke Shao: looks good to me
Dexter Wei: Thanks.
Ke Shao: so that's the end of the coding part. do you have any question about the company for me?
Dexter Wei: Yes. I am interested in what project are you mainly in charge of?
Ke Shao: so our company mainly working on two parts
Dexter Wei: To my knowledge, Fresh Digital Group is the software company that provides voice assistance solution.
Ke Shao: one part is develop voice skill for google home, amazon alexa, and microsoft cortana
Ke Shao: the other part is a data management platform, which basically is a website.
Dexter Wei: That is very cool.
Ke Shao: underneath, it is a database collecting the voice skill data coming from users
Ke Shao: so the voice skill mainly written in nodeJS, and the database is using ruby on rails
Ke Shao: Does this answer your question?
Dexter Wei: Yes, it is.
Ke Shao: Cool
Ke Shao: Any other question?
Dexter Wei: Yes, there is one more. May I be informed of the next schedule in procedures, please?
Ke Shao: I think maybe within three business days, our HR will contact you. Maybe there will be some behavioural questions, or not.
Dexter Wei: OK, understood.
Dexter Wei: I am done with questions.
Ke Shao: Great
Ke Shao: so this is the end of the interview
Dexter Wei: Thank you for your time and consideration. Look forward to the next.
Dexter Wei: OK. Take care. Be safe in storm.
Ke Shao: It's been nice chating to you, Dexter
Ke Shao: Thanks, have a good one
Dexter Wei: Thank you. You too. See you.
Ke Shao: See you
"""

"""
Question:
     
    Given a binary tree, find its maximum depth.
    
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
 
def find_max_depth(root_node, max_depth = 0):
    """
     Inputs - root_node, take in the root node of a binary tree
              max_depth, initialize 0
     
     Output - return the maximum depth as integer
    """
    if root_node is None:
        return max_depth
    return max(find_max_depth(root_node.left, max_depth + 1), find_max_depth(root_node.right, max_depth + 1))
