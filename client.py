import tkinter as tk
import os
import reaction_tester, graph
win = tk.Tk()

win.geometry("1200x720")
win.configure(bg=("black"))
win.title("Client")

def start_reaction_test():
    reaction_tester.reaction_tester_main()

    
def start_graph():
    graph.graph_main()

def main():
    reaction_tester_button = tk.Button(win, background='green', 
                            font=('Comic Sans', 50), text="Reaction Test!", command=start_reaction_test)
    graph_button = tk.Button(win, background='red', 
                            font=('Comic Sans', 50), text="Graph your reaction!", command=start_graph)


    reaction_tester_button.pack(anchor=tk.W, padx=50, pady=50)

    graph_button.pack(anchor=tk.E, padx=50, pady=50)

    win.mainloop()

if __name__ == '__main__':
    main()
