from collections.abc import Callable, Iterable, Mapping
from threading import Thread, Condition
from typing import Any
import socket, inspect
from calculus.spreadsheet import Calculus, DESCRIPTIONS

def convert_args(param, arg: str | list):
    # Check if the annotation is a union of int and float
    if hasattr(param.annotation, "__args__") and float in param.annotation.__args__:
        return float(arg)
    return param.annotation(arg)

class Connection(Thread):
    _connected_clients = 0
    def __init__(self, conn: socket.socket, addr: tuple[str, int], cond: Condition, 
                 group: None = None, target: Callable[..., object] | None = None, name: str | None = None, 
                 args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        # You can just ignore most of the original arguments of the class Thread from threading
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.conn = conn
        self.addr = addr
        with cond:
            # threading.Condition objects supports the context manager type, so you can use it in a with statement. 
            # There’s no need to call .acquire() and .realease():
            Connection._connected_clients += 1
              
    def handle_client(self) -> None:
        print(f"Connection etablished with {self.addr}")
        # A dict refering all the available functions for this calculus server
        functions = {
            "1": Calculus.factorial,
            "2": Calculus.catalan,
            "3": Calculus.floor,
            "4": Calculus.ceil,
            "5": Calculus.are_divisible,
            "6": Calculus.list_div,
            "7": Calculus.is_prime,
            "8": Calculus.primelist,
            "9": Calculus.digitsum,
            "10": Calculus.all_negative,
            "11": Calculus.all_positive,
            "12": Calculus.all_null,
            "13": Calculus.Zeller_algorithm,
            "14": Calculus.gcd,
            "15": Calculus.lcm,
            "quit": exit
        }
        function_names = {
            "1": "factorial",
            "2": "catalan",
            "3": "floor",
            "4": "ceil",
            "5": "are_divisible",
            "6": "list_div",
            "7": "is_prime",
            "8": "primelist",
            "9": "digitsum",
            "10": "all_negative",
            "11": "all_positive",
            "12": "all_null",
            "13": "Zeller_algorithm",
            "14": "greatest common divisor",
            "15": "least common multiple"
        }
        formated_description = "".join(descrip for descrip in DESCRIPTIONS)
        self.conn.sendall(f"Welcome on our calculus server dear client. Please choose one of this options as a service by choosing the corresponding key or type 'quit' to end the connection\n{formated_description}".encode())
        while True:
            # Wait client response
            response = self.conn.recv(2048).decode().strip()
            if response.startswith("q"):
                self.conn.close()
                break    
            while response not in functions.keys():
                self.conn.sendall(f"Sorry we don't have any service with this key: {response}. Please choose another option\n".encode())
                # Wait client response
                response = self.conn.recv(2048).decode().strip()
                if response.startswith("q"):
                    self.conn.close()
                    break
                            
            requiered_args = inspect.signature(functions[response]).parameters
            num_args = "a list of" if response in ("10", "11", "12") else len(requiered_args)
            self.conn.sendall(f"The function you want to run needs {num_args} arguments. Please type them one by one separated by spaces (exemple: arg1 arg2).\n".encode())
            args = self.conn.recv(2048).decode().strip()
            if response.startswith("q"):
                self.conn.close()
                break
            args = args.split()
            # Convert arguments fit them in the corresponding functions
            if response in ("10", "11", "12"):
                # Put the converted list of args in a tuple
                converted_args = ([float(arg) for arg in args],)
            else: converted_args = (convert_args(param=param, arg=arg) for param, arg in zip(requiered_args.values(), args))
            returned = functions[response](*converted_args)
            self.conn.sendall(f"Returned: {returned} for function {function_names[response]} with args {args}\nAny other service?\n".encode())
            
    def start(self) -> None:
        self.handle_client()
                   