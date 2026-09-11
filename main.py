from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.08, 0.12, 1)


class RiskCalc(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        scroll = ScrollView()
        form = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        form.bind(minimum_height=form.setter('height'))

        form.add_widget(Label(text="[b]Risk Calculator[/b]", markup=True,
                              font_size=26, size_hint_y=None, height=50))

        self.balance = self.make_input(form, "Account Balance ($)", "1000")
        self.risk = self.make_input(form, "Risk %", "1")
        self.entry = self.make_input(form, "Entry Price", "100")
        self.sl = self.make_input(form, "Stop Loss", "95")
        self.tp = self.make_input(form, "Take Profit", "115")

        btn = Button(text="CALCULATE", size_hint_y=None, height=60,
                     background_color=(0.1, 0.7, 0.3, 1))
        btn.bind(on_press=self.calculate)
        form.add_widget(btn)

        self.result = Label(text="", markup=True, font_size=18,
                            size_hint_y=None, height=300)
        form.add_widget(self.result)

        scroll.add_widget(form)
        self.add_widget(scroll)

    def make_input(self, parent, label, default):
        parent.add_widget(Label(text=label, size_hint_y=None, height=30))
        ti = TextInput(text=default, multiline=False,
                       input_filter='float', size_hint_y=None, height=45)
        parent.add_widget(ti)
        return ti

    def calculate(self, *args):
        try:
            bal = float(self.balance.text)
            rk = float(self.risk.text)
            en = float(self.entry.text)
            sl = float(self.sl.text)
            tp = float(self.tp.text)

            risk_amt = bal * (rk / 100)
            stop_dist = abs(en - sl)
            pos_size = risk_amt / stop_dist if stop_dist else 0
            rr = (tp - en) / (en - sl) if (en - sl) else 0
            profit = (tp - en) * pos_size
            loss = (en - sl) * pos_size

            self.result.text = (
                f"[b]Risk Amount:[/b] ${risk_amt:.2f}\n"
                f"[b]Position Size:[/b] {pos_size:.4f} units\n"
                f"[b]Risk/Reward:[/b] 1:{rr:.2f}\n\n"
                f"[color=00ff88]Potential Profit: ${profit:.2f}[/color]\n"
                f"[color=ff5555]Potential Loss: ${loss:.2f}[/color]"
            )
        except:
            self.result.text = "[color=ff5555]Check your numbers.[/color]"


class RiskCalcApp(App):
    def build(self):
        return RiskCalc()


if __name__ == "__main__":
    RiskCalcApp().run()
