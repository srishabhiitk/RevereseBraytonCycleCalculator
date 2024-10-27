from PySide6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from plotter import MplCanvas
import sys
import numpy as np



class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.add_plots_to_gui()

        self.save_PB.clicked.connect(self.change_plot)
        self.InletPressureSlider.valueChanged.connect(self.connect_slider_to_buttonIP)
        self.InletPressureSB.valueChanged.connect(self.connect_button_to_sliderIP)
        self.InletTempSlider.valueChanged.connect(self.connect_slider_to_buttonIT)
        self.InletTempSB.valueChanged.connect(self.connect_button_to_sliderIT)
        self.pressureRatioSlider.valueChanged.connect(self.connect_slider_to_buttonPR)
        self.PressureRatioSB.valueChanged.connect(self.connect_button_to_sliderPR)
        self.inputVolSlider.valueChanged.connect(self.connect_slider_to_buttonIV)
        self.inputVolSB.valueChanged.connect(self.connect_button_to_sliderIV)
        self.T3Slider.valueChanged.connect(self.connect_slider_to_buttonT3)
        self.T3SB.valueChanged.connect(self.connect_button_to_sliderT3)


    def add_plots_to_gui(self):
        self.TSplot = MplCanvas(self, width=5, height=4, dpi=100)
        self.TSplot.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.verticalLayout_3.addWidget(self.TSplot)

        self.PVplot = MplCanvas(self, width=5, height=4, dpi=100)
        self.PVplot.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.verticalLayout_3.addWidget(self.PVplot)

    def connect_slider_to_buttonIP(self, data):
        self.InletPressureSB.setValue(data)
    
    def connect_button_to_sliderIP(self, data):
        self.InletPressureSlider.setValue(data)
    
    def connect_slider_to_buttonIT(self, data):
        self.InletTempSB.setValue(data)
    
    def connect_button_to_sliderIT(self, data):
        self.InletTempSlider.setValue(data)

    def connect_slider_to_buttonPR(self, data):
        self.PressureRatioSB.setValue(data)
    
    def connect_button_to_sliderPR(self, data):
        self.pressureRatioSlider.setValue(data)

    def connect_slider_to_buttonIV(self, data):
        self.inputVolSB.setValue(data)
    
    def connect_button_to_sliderIV(self, data):
        self.inputVolSlider.setValue(data)
    
    def connect_slider_to_buttonT3(self, data):
        self.T3SB.setValue(data)
    
    def connect_button_to_sliderT3(self, data):
        self.T3Slider.setValue(data)


    def change_plot(self):
        T_1 = self.InletTempSB.value() # Input Temperature in kelvin
        P_1 = self.InletPressureSB.value() # input Pressure in kPa
        gamma = self.gammaSB.value() # ratio of Specific heats
        c_p   = self.cpSB.value() # Constant pressure Specific Heat in kJ/Kg K
        R = self.rSB.value()  # Standard value at 25 deg C, in kJ/(kg K)
        T_0 = 200  # The reference temperature for entropy
        P_0 =  100  # The reference pressure for entropy
        r_p =  self.PressureRatioSB.value() #  Pressure ratio
        V_1  = self.inputVolSB.value() # Input volume in cc
        T_3 = self.T3SB.value() # Temperature after heat exchange
        P_2  = P_1  * r_p 
        T_2 = T_1 * (r_p **((gamma -1)/gamma))
        V_2 = V_1 * (1/r_p)**(1/gamma)
        # T_3 = q_in/c_p + T_2
        P_3 = P_2 
        V_3 = (T_3/T_2)* V_2
        T_4 = T_3 / (r_p **((gamma -1)/gamma))
        P_4 = P_1
        V_4 = (r_p**(1/gamma)) * V_3 
        eta = 1  - 1/(r_p **((gamma -1)/gamma))
        c_1 = (P_2 * V_2**gamma)
        c_3 = (P_3* V_3**gamma)
        s_1 = (c_p * np.log( T_1/T_0)) - ( R * (np.log (P_1/P_0)))
        s_2  = (c_p * np.log( T_2/T_0)) - ( R * (np.log (P_2/P_0)))
        s_3  = (c_p * np.log( T_3/T_0)) - ( R * (np.log (P_3/P_0)))
        s_4  =  (c_p * np.log( T_3/T_0)) - ( R * (np.log (P_3/P_0)))

        # print('clear plot')
        self.PVplot.axes.cla()
        T = np.zeros(20)
        P = np.zeros(50)
        V = np.zeros(50)
        P = np.linspace (P_1, P_2, 50)
        V = ((c_1/P)**(1/gamma))

        self.PVplot.axes.plot(V,P,"r")

        T = np.zeros(50)
        P = np.zeros(50)
        V = np.zeros(50)
        T = np.linspace(T_2, T_3, 50)
        P = np.linspace (P_2, P_3, 50)
        V = np.linspace (V_2, V_3, 50)
        self.PVplot.axes.plot(V,P,"r")

        T = np.zeros(50)
        P = np.zeros(50)
        V = np.zeros(50)
        T = np.linspace(T_3, T_4, 50)
        P = np.linspace (P_3, P_4, 50)
        V = ((c_3/P)**(1/gamma))
        self.PVplot.axes.plot(V,P,"r")

        T = np.zeros(50)
        P = np.zeros(50)
        V = np.zeros(50)
        T = np.linspace(T_4, T_1, 50)
        P = np.linspace (P_4, P_1, 50)
        V = np.linspace (V_4, V_1, 50)
        self.PVplot.axes.plot(V,P,"r")
        self.PVplot.axes.set_title("P-V Diagram of Brayton cycle")
        self.PVplot.axes.set_xlabel('Volume in CC')
        self.PVplot.axes.set_ylabel('Pressure in kPa')

        self.PVplot.axes.grid(ls='--')
        self.PVplot.draw()

        self.TSplot.axes.cla()

        T = np.zeros(50)
        T = np.linspace(T_1, T_2, 50)
        s = s_1 * np.ones(50)
        self.TSplot.axes.plot (s,T,"b")

        T = np.linspace(T_2,T_3,50)
        P = np.linspace (P_2, P_3, 50)
        s = (c_p * np.log( T/T_2))   - ( R * ( np.log (P/P_2))) + s_1
        self.TSplot.axes.plot(s,T,"b")

        T = np.linspace(T_3,T_4,50)
        s = s_3 * np.ones(50)
        self.TSplot.axes.plot(s,T,"b")

        T = np.linspace(T_4,T_1,50)
        P = np.linspace (P_4, P_1, 50)
        s = s_3 + (c_p * np.log( T/T_4))   - ( R * ( np.log (P/P_4)))  
        self.TSplot.axes.plot(s,T,"b")
        self.TSplot.axes.set_ylabel("Temperature in Kelvin ")
        self.TSplot.axes.set_xlabel('Specific Entropy in kJ / (Kg K)')
        self.TSplot.axes.set_title('Plot of Temperature vs Specific Entropy ')
        self.TSplot.axes.grid(ls='--')
        self.TSplot.draw()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
