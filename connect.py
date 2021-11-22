import tkinter as tk
import StartPage
import MenuPage


class SampleApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top", fill="both" ,expand=True)
		container.grid_rowconfigure(0, weight =1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		for F in (StartPage.StartPage,MenuPage.MenuPage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame("StartPage")
	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

		
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    
