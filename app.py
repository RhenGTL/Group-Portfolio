from flask import Flask, render_template, request, session
from flask_session import Session
import timeit, random, re
from math import pi
from linear_search import linear_search, linear_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from exponential_search import exponential_search, exponential_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ardon')
def ardon():
    return render_template('ardon.html')

@app.route('/austria')
def austria():
    return render_template('austria.html')

@app.route('/faustino')
def faustino():
    return render_template('faustino.html')

@app.route('/garcia')
def garcia():
    return render_template('garcia.html')

@app.route('/gustilo')
def gustilo():
    return render_template('gustilo.html')

@app.route('/melitante')
def melitante():
    return render_template('melitante.html')

@app.route('/moreno')
def moreno():
    return render_template('moreno.html')

@app.route('/ramos')
def ramos():
    return render_template('ramos.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('uppercase.html', result=result)

@app.route('/circle_area', methods=['GET', 'POST'])
def circle_area():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', type=float)
        if radius is not None and radius > 0:
            result = str(round(pi * radius * radius, 4)) + ' sq. units'
        else:
            result = 'Invalid radius'
    return render_template('circle_area.html', result=result)

@app.route('/triangle_area', methods=['GET', 'POST'])
def triangle_area():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', type=float)
        height = request.form.get('height', type=float)
        if base is not None and base > 0 and height is not None and height > 0:
            result = str(round(0.5 * base * height, 4)) + ' sq. units'
        else:
            result = 'Invalid base or height'
    return render_template('triangle_area.html', result=result)

@app.route("/search_algo", methods=["GET", "POST"])
def search_algo():
    size = 100

    if 'dataset' not in session:
        data = sorted(range(1, size + 1))
        session['dataset'] = ", ".join(map(str, data))
        session['target'] = random.choice(data)
        session['size'] = size

    if request.method == "POST":
        if 'generate' in request.form:
            size = int(request.form.get('size'))
            data = sorted(range(1, size + 1))
            session['dataset'] = ", ".join(map(str, data))
            session['target'] = random.choice(data)

        elif 'search' in request.form:
            array_str = session['dataset']  
            search_type = request.form.get("search_type")   
            
            try:
                size = int(request.form.get("size"))    
                array = list(map(int, array_str.split(", ")))   
                target = int(request.form.get("target"))
                low, high = 0, len(array) - 1

                if search_type == "linear":
                    execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = linear_search_wrapper(linear_search, array, target)  
                elif search_type == "binary":
                    execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = binary_search_wrapper(binary_search, array, target)
                elif search_type == "ternary":
                    execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target,"low":low,"high":high}, number=1)  * 1000 
                    result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                elif search_type == "exponential":
                    execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = exponential_search_wrapper(exponential_search, array, target)
                elif search_type == "interpolation":
                    execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = interpolation_search_wrapper(interpolation_search, array, target) 
                elif search_type == "jump":
                    execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = jump_search_wrapper(jump_search, array, target)  

                return render_template("search_algo.html", array=array, target=target, result=result, execution_time=execution_time, size=size, dataset=session['dataset'], search_type=search_type)
                
            except ValueError:
                return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.", dataset=session['dataset'], size=size, search_type=search_type)
        
        elif 'edit' in request.form:
            session['dataset'] = request.form.get('array')
  
    return render_template("search_algo.html", dataset=session['dataset'], size=size, target=session['target'])

@app.route('/merge_list', methods=['GET', 'POST'])
def merge_list():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class Stack:
        def __init__(self):
            self.top = None

        def merge_push(self, data):
            new_node = Node(data)
            if self.top:
                new_node.next = self.top
            self.top = new_node

        def push(self, data):
            if -100 <= data <= 100:
                new_node = Node(data)
                if self.top:
                    new_node.next = self.top
                self.top = new_node
            else:
                return "data range must be -100 to 100"
            
        def pop(self):
            if self.top:
                popped_node = self.top
                self.top = self.top.next
                return popped_node.data
            return "stack is empty"
            
        def peek(self):
            if self.top:
                return self.top.data
            return "stack is empty"
        
        def is_empty(self):
            return self.top is None
        
        def print_stack(self):
            current_node=self.top
            stack_elements = []
            while current_node:
                stack_elements.append(current_node.data)
                current_node=current_node.next
            return stack_elements

        def stack_size(self):
            current_node = self.top
            count = 0
            while current_node:
                count += 1
                current_node = current_node.next
            return count
        
        def pop_max(self):
            if self.is_empty():
                return "empty list detected"
            max_value = -float('inf')
            current_node = self.top
            prev_node = None
            max_node = self.top
            prev_max_node = None

            while current_node:
                if current_node.data > max_value:
                    max_value = current_node.data
                    prev_max_node = prev_node
                    max_node = current_node
                prev_node = current_node
                current_node = current_node.next

            if max_node == self.top:
                self.top = self.top.next
            else:
                prev_max_node.next = max_node.next

            return max_value
    
    def merge_stacks(stack1, stack2):
        merged = Stack()
        stack1_value = stack1.pop_max() if not stack1.is_empty() else None
        stack2_value = stack2.pop_max() if not stack2.is_empty() else None
        while stack1_value is not None or stack2_value is not None:
            if stack1_value is None:
                merged.merge_push(stack2_value)
                stack2_value = stack2.pop_max() if not stack2.is_empty() else None
            elif stack2_value is None:
                merged.merge_push(stack1_value)
                stack1_value = stack1.pop_max() if not stack1.is_empty() else None
            elif stack1_value > stack2_value:
                merged.merge_push(stack1_value)
                stack1_value = stack1.pop_max() if not stack1.is_empty() else None
            else:
                merged.merge_push(stack2_value)
                stack2_value = stack2.pop_max() if not stack2.is_empty() else None
        return merged

    result = None
    if request.method == 'POST':
        list1 = request.form.get('list1', type=str).split()
        list2 = request.form.get('list2', type=str).split()
        if len(list1) == 0 or len(list2) == 0:
            result = 'empty list detected'
        elif len(list1) > 50 or len(list2) > 50:
            result = 'max list size is 50'
        else:
            try:
                stack1 = Stack()
                stack2 = Stack()
                for i in list1:
                    push_result = stack1.push(int(i))
                    if push_result:
                        result = push_result
                        break
                for i in list2:
                    if result is not None:
                        break
                    push_result = stack2.push(int(i))
                    if push_result:
                        result = push_result
                        break
            except ValueError:
                result = 'non-integer value detected'
                    
            if result is None:
                merged_list = merge_stacks(stack1, stack2)
                result = " -> ".join(map(str, merged_list.print_stack()))
            
    return render_template('merge_list.html', result=result)

@app.route('/infix_postfix', methods=['GET', 'POST'])
def infix_postfix():
    class Node:
        def __init__(self, data):
            self.data= data
            self.next= None

    class Stack:
        def __init__(self):
            self.top = None

        def push(self, data):
            new_node = Node(data)
            if self.top:
                new_node.next = self.top
            self.top = new_node
        
        def pop(self):
            if self.top is None:
                return None
            else:
                popped_node = self.top
                self.top = self.top.next
                popped_node.next = None
                return popped_node.data
        
        def peek(self):
            if self.top:
                return self.top.data
            else:
                return None

    def get_precedence(operator):
        if operator == '^':
            return 3
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        else:
            return 0
        
    def isoperator(token):
        return token == '^' or token == '*' or token == '/' or token == '+' or token == '-'

    def infix_to_postfix(infix_expression):
        operator = Stack()
        output = Stack()

        for token in infix_expression:
            if token.isalnum():             
                output.push(token)
            elif token == '(':              
                operator.push(token)
            elif token == ')':              
                while operator.peek() != "(":
                    output.push(operator.pop())
                operator.pop()
            elif isoperator(token):         
                while operator.peek() != None and get_precedence(operator.peek()) >= get_precedence(token):
                    output.push(operator.pop())
                operator.push(token)
            
        while operator.peek() != None:
            output.push(operator.pop())

        result = []
        while output.peek() != None:
            result.append(output.pop())
        result.reverse()
        
        return ''.join(result)
    
    def is_valid_infix(expression):
        expression = expression.replace(' ', '')
        open_parentheses = 0
        operators = 0
        operands = 0
        for char in expression:
            if char == '(':
                open_parentheses += 1
            if char == ')':
                open_parentheses -= 1
            if open_parentheses < 0:
                return False
            if isoperator(char):
                operators += 1
            if char.isalnum():
                operands += 1
        if open_parentheses != 0 or operators < 1 or operands < 2:
            return False
        
        previous_char = None
        for char in expression:
            if isoperator(char):
                if previous_char is None or previous_char == '(' or isoperator(previous_char):
                    return False
            elif char.isalnum():
                if previous_char is not None and (previous_char.isalnum() or previous_char == ')'):
                    return False
            elif char == '(':
                if previous_char is not None and (previous_char.isalnum() or previous_char == ')'):
                    return False
            elif char == ')':
                if previous_char is None or previous_char == '(' or isoperator(previous_char):
                    return False
            previous_char = char

        return True
    
    result = None
    if request.method == 'POST':
        infix_exp = request.form.get('infix', type=str)
        if re.match("^[A-za-z0-9+\-*/()^ ]*$", infix_exp) and is_valid_infix(infix_exp):
            result = infix_to_postfix(infix_exp)
        else:
            result = "Invalid infix expression."
        
    return render_template('infix_postfix.html', result=result)

@app.route('/queue_dequeue', methods=['GET', 'POST'])
def queue_dequeue():
    request_method = request.method

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class Queue:
        def __init__(self):
            self.front = None
            self.back = None
            self.length = 0

        def is_empty(self):
            return self.length == 0

        def push(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.front = new_node
            else:
                self.back.next = new_node
            self.back = new_node
            self.length += 1
            return data
        
        def pop(self):
            if self.is_empty():
                return None
            else:
                popped_node = self.front
                self.front = popped_node.next
                popped_node.next = None

                if self.front is None:
                    self.back = None

                self.length -= 1 
                return popped_node.data
        
        def peek(self):
            if self.front:
                return self.front.data
            else:
                return None
            
        def size(self):
            return self.length
        
        def serialize(self):
            node = self.front
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            return nodes

        @classmethod
        def deserialize(cls, nodes):
            queue = cls()
            for node in nodes:
                queue.push(node)
            return queue
        
    class Dequeue:
        def __init__(self):
            self.front = None
            self.back = None
            self.length = 0
        
        def is_empty(self):
            return self.length == 0
        
        def push_front(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.back = new_node
            else:
                new_node.next = self.front
                self.front.prev = new_node
            self.front = new_node
            self.length += 1
            return data

        def push_back(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.front = new_node
            else:
                new_node.prev = self.back
                self.back.next = new_node
            self.back = new_node
            self.length += 1
            return data

        def pop_front(self):
            if self.is_empty():
                return None
            else:
                popped_node = self.front
                self.front = popped_node.next
                popped_node.next = None

                if self.front is None:
                    self.back = None
                else:
                    self.front.prev = None

                self.length -= 1 
                return popped_node.data

        def pop_back(self):
            if self.is_empty():
                return None
            else:
                popped_node = self.back
                self.back = popped_node.prev
                popped_node.prev = None

                if self.back is None:
                    self.front = None
                else:
                    self.back.next = None

                self.length -= 1 
                return popped_node.data

        def peek_front(self):
            if self.front:
                return self.front.data
            else:
                return None

        def peek_back(self):
            if self.back:
                return self.back.data
            else:
                return None

        def size(self):
            return self.length
        
        def serialize(self):
            node = self.front
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            return nodes

        @classmethod
        def deserialize(cls, nodes):
            dequeue = cls()
            for node in nodes:
                dequeue.push_back(node)
            return dequeue
    
    if request.method == 'GET':
        session.clear()
        session['queue_list'] = Queue().serialize()
        session['dequeue_list'] = Dequeue().serialize()

    if 'queue_list' not in session:
        session['queue_list'] = Queue().serialize()
    if 'dequeue_list' not in session:
        session['dequeue_list'] = Dequeue().serialize()

    queue_list = Queue.deserialize(session['queue_list'])
    dequeue_list = Dequeue.deserialize(session['dequeue_list'])

    queue_result = None
    dequeue_result = None
    queueAction = None
    queueInput = None
    dequeueAction = None
    dequeueInput = None
    
    if request.method == 'POST':
        if 'queue_submit' in request.form:
            queueAction = request.form.get('queue_action', type=str)
            queueInput = request.form.get('queue_input', type=str)

            if queueAction == None:
                queue_result = "Please select an action."
            elif queueAction == 'push':
                if queueInput == "":
                    queue_result = "Please enter a data."
                else:
                    queue_result = queue_list.push(queueInput)
            elif queueAction == 'pop':
                queue_result = queue_list.pop()
            elif queueAction == 'peek':
                queue_result = queue_list.peek()
            elif queueAction == 'queue_size':
                queue_result = queue_list.size()
                if queue_result == 0:
                    queue_result = "List is empty."

            if queue_result is None and (queueAction == 'pop' or queueAction == 'peek'):
                    queue_result = "List is empty."

        if 'dequeue_submit' in request.form:
            dequeueAction = request.form.get('dequeue_action', type=str)
            dequeueInput = request.form.get('dequeue_input', type=str)

            if dequeueAction == None:
                dequeue_result = "Please select an action."
            elif dequeueAction == 'push_front':
                if dequeueInput == "":
                    dequeue_result = "Please enter a data."
                else:
                    dequeue_result = dequeue_list.push_front(dequeueInput)
            elif dequeueAction == 'push_back':
                if dequeueInput == "":
                    dequeue_result = "Please enter a data."
                else:
                    dequeue_result = dequeue_list.push_back(dequeueInput)
            elif dequeueAction == 'pop_front':
                dequeue_result = dequeue_list.pop_front()
            elif dequeueAction == 'pop_back':
                dequeue_result = dequeue_list.pop_back()
            elif dequeueAction == 'peek_front':
                dequeue_result = dequeue_list.peek_front()
            elif dequeueAction == 'peek_back':
                dequeue_result = dequeue_list.peek_back()
            elif dequeueAction == 'dequeue_size':
                dequeue_result = dequeue_list.size()
                if dequeue_result == 0:
                    dequeue_result = "List is empty."
            
            if dequeue_result is None and (dequeueAction == 'pop_front' or dequeueAction == 'pop_back' or dequeueAction == 'peek_front' or dequeueAction == 'peek_back'):
                    dequeue_result = "List is empty."

    session['queue_list'] = queue_list.serialize()
    session['dequeue_list'] = dequeue_list.serialize()
            
    return render_template('queue_dequeue.html', reset_slider=True, queue_result=queue_result, queueAction=queueAction, queueInput=queueInput, dequeue_result=dequeue_result, dequeueAction=dequeueAction, dequeueInput=dequeueInput, request_method=request_method)

if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(debug=True)
