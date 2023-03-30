import ipywidgets as widgets

import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')

# from schemdraw import logic

class visualizaton:
    def __init__(self) -> None:
        pass

    def plot_single_bloc(self, r1=0, r2=0, r3=0, r4=0, r5=0, r6=0, r7=0, r8=0, r9=0, r10=0, r11=0, r12=0, r13=0, r14=0, r15=0, r16=0, r17=0, r18=0, r19=0,
                         r20=0, r21=0, r22=0, r23=0, r24=0, r25=0, r26=0, r27=0, r28=0, r29=0, r30=0):
        with schemdraw.Drawing(show=False) as heat:
            heat.config(unit=1)
            heat += elm.Line().down(heat.unit * 0.2)
            heat += elm.Line().right()
            heat += elm.Line().up(heat.unit * 0.2)
            heat.push()
            heat += elm.Line().up(heat.unit * 0.2)
            heat += elm.Line().left()
            heat += elm.Line().down(heat.unit * 0.4)
            heat += elm.Line().right(heat.unit * 0.25)
            heat += elm.Line().up(heat.unit * 0.4)
            heat += elm.Line().right(heat.unit * 0.25)
            heat += elm.Line().down(heat.unit * 0.4)
            heat += elm.Line().right(heat.unit * 0.25)
            heat += elm.Line().up(heat.unit * 0.4)
            heat.pop()
            heat += elm.Line().right(heat.unit * 0.1)

        with schemdraw.Drawing(show=False) as power:
            power.config(unit=3)

            power += elm.SourceV().right().label('12V\n10A\n№1')
            power += elm.Line().down()
            power.push()
            power += elm.SourceV().left().label('12V\n10A\n№2')
            power.pop()
            power += elm.Line().down()
            power.push()
            power += elm.SourceV().left().label('12V\n10A\n№3')
            power.pop()
            power += elm.Line().down()
            power.push()
            power += elm.SourceV().left().label('12V\n10A\n№4')
            power.pop()
            power += elm.Line().down()
            power += elm.Line().right()

        with schemdraw.Drawing(show=False) as relay_open:
            relay_open.config(unit=3)

            relay_open += (rel1 := elm.compound.Relay(unit=2, link=True)).left().anchor('a')
            # unit: float = 2, cycl: bool = False, switch: str = 'spst',
            # core: bool = True, box: bool = True, boxfill: str = 'none',
            # boxpad: float = 0.25, swreverse: bool = False, swflip: bool = False,
            # link: bool = True)
            relay_open.push()
            relay_open += elm.Switch(action='open').idot().up(relay_open.unit * 0.67)
            relay_open.pop()

            relay_open += elm.Line().up().at(rel1.b)
            relay_open += elm.MeterA().up().label(str(12) + 'A')
            relay_open += elm.Line().up(relay_open.unit * 0.1)
            relay_open += elm.ElementDrawing(heat).up()

            relay_open += elm.Line().right(relay_open.unit).at(rel1.a).idot()

        with schemdraw.Drawing(show=False) as relay_close:
            relay_close.config(unit=3)

            relay_close += (rel1 := elm.compound.Relay(unit=2, link=False)).left().anchor('a')
            relay_close.push()
            relay_close += elm.Switch(action='close').idot().up(relay_close.unit * 0.67)
            relay_close.pop()

            relay_close += elm.Line().up().at(rel1.b)
            relay_close += elm.MeterA().up().label(str(12) + 'A')
            relay_close += elm.Line().up(relay_close.unit * 0.1).label('1')
            relay_close += elm.ElementDrawing(heat).up()

            relay_close += elm.Line().right(relay_close.unit).at(rel1.a).idot()

        with schemdraw.Drawing(show=False) as relay_open_down:
            relay_open_down.config(unit=3)

            relay_open_down += (rel1 := elm.compound.Relay(unit=2, link=True)).left().anchor('a')
            # unit: float = 2, cycl: bool = False, switch: str = 'spst',
            # core: bool = True, box: bool = True, boxfill: str = 'none',
            # boxpad: float = 0.25, swreverse: bool = False, swflip: bool = False,
            # link: bool = True)
            relay_open_down.push()
            relay_open_down += elm.Switch(action='open').idot().up(relay_open_down.unit * 0.67)
            relay_open_down.pop()

            relay_open_down += elm.Line().up().at(rel1.b)
            relay_open_down += elm.MeterA().up().label(str(12) + 'A')
            relay_open_down += elm.Line().up(relay_open_down.unit * 0.1)
            relay_open_down += elm.ElementDrawing(heat).up()

            relay_open_down += elm.Line().right(relay_open_down.unit).at(rel1.a).idot()

        with schemdraw.Drawing(show=False) as relay_close_down:
            relay_close_down.config(unit=3)

            relay_close_down += (rel1 := elm.compound.Relay(unit=2, link=False)).left().anchor('a')
            relay_close_down.push()
            relay_close_down += elm.Switch(action='close').idot().up(relay_close_down.unit * 0.67)
            relay_close.pop()

            relay_close_down += elm.Line().up().at(rel1.b)
            relay_close_down += elm.MeterA().up().label(str(12) + 'A')
            relay_close_down += elm.Line().up(relay_close_down.unit * 0.1).label('1')
            relay_close_down += elm.ElementDrawing(heat).up()

            relay_close_down += elm.Line().right(relay_close_down.unit).at(rel1.a).idot()

        with schemdraw.Drawing(show=True) as d:

              # Set the backend here

            d = schemdraw.Drawing()
            import matplotlib
            matplotlib.use('Agg')
            d.config(unit=3)

            d += elm.ElementDrawing(power)

            d += elm.Line().left()
            d.push()
            d += elm.Line().right()

            r_up = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]

            for i in range(len(r_up)):
                if r_up[i]:
                    d += elm.ElementDrawing(relay_open).label('№' + str(i + 1))
                else:
                    d += elm.ElementDrawing(relay_close)

            d.pop()
            d += elm.Line().down()

            r_down = [r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30]

            for i in range(len(r_down)):
                if r_down[i]:
                    d += elm.ElementDrawing(relay_open).label('№' + str(i + 16))
                else:
                    d += elm.ElementDrawing(relay_close)

            d.save('static/img/scheme.svg')
            print('Successfully saved image')

    def interact_plot(self):
        r1 = widgets.Checkbox(
            value=True, description='Реле 1', disabled=False, indent=False)
        r2 = widgets.Checkbox(
            value=True, description='Реле 2', disabled=False, indent=False)
        r3 = widgets.Checkbox(
            value=True, description='Реле 3', disabled=False, indent=False)
        r4 = widgets.Checkbox(
            value=True, description='Реле 4', disabled=False, indent=False)
        r5 = widgets.Checkbox(
            value=True, description='Реле 5', disabled=False, indent=False)
        r6 = widgets.Checkbox(
            value=True, description='Реле 6', disabled=False, indent=False)
        r7 = widgets.Checkbox(
            value=True, description='Реле 7', disabled=False, indent=False)
        r8 = widgets.Checkbox(
            value=True, description='Реле 8', disabled=False, indent=False)
        r9 = widgets.Checkbox(
            value=True, description='Реле 9', disabled=False, indent=False)
        r10 = widgets.Checkbox(
            value=True, description='Реле 10', disabled=False, indent=False)
        r11 = widgets.Checkbox(
            value=True, description='Реле 11', disabled=False, indent=False)
        r12 = widgets.Checkbox(
            value=True, description='Реле 12', disabled=False, indent=False)
        r13 = widgets.Checkbox(
            value=True, description='Реле 13', disabled=False, indent=False)
        r14 = widgets.Checkbox(
            value=True, description='Реле 14', disabled=False, indent=False)
        r15 = widgets.Checkbox(
            value=True, description='Реле 15', disabled=False, indent=False)
        r16 = widgets.Checkbox(
            value=True, description='Реле 16', disabled=False, indent=False)
        r17 = widgets.Checkbox(
            value=True, description='Реле 17', disabled=False, indent=False)
        r18 = widgets.Checkbox(
            value=True, description='Реле 18', disabled=False, indent=False)
        r19 = widgets.Checkbox(
            value=True, description='Реле 19', disabled=False, indent=False)
        r20 = widgets.Checkbox(
            value=True, description='Реле 20', disabled=False, indent=False)
        r21 = widgets.Checkbox(
            value=True, description='Реле 21', disabled=False, indent=False)
        r22 = widgets.Checkbox(
            value=True, description='Реле 22', disabled=False, indent=False)
        r23 = widgets.Checkbox(
            value=True, description='Реле 23', disabled=False, indent=False)
        r24 = widgets.Checkbox(
            value=True, description='Реле 24', disabled=False, indent=False)
        r25 = widgets.Checkbox(
            value=True, description='Реле 25', disabled=False, indent=False)
        r26 = widgets.Checkbox(
            value=True, description='Реле 26', disabled=False, indent=False)
        r27 = widgets.Checkbox(
            value=True, description='Реле 27', disabled=False, indent=False)
        r28 = widgets.Checkbox(
            value=True, description='Реле 28', disabled=False, indent=False)
        r29 = widgets.Checkbox(
            value=True, description='Реле 29', disabled=False, indent=False)
        r30 = widgets.Checkbox(
            value=True, description='Реле 30', disabled=False, indent=False)

        out = widgets.interactive_output(self.plot_single_bloc, {
            'r1': r1,
            'r2': r2,
            'r3': r3,
            'r4': r4,
            'r5': r5,
            'r6': r6,
            'r7': r7,
            'r8': r8,
            'r9': r9,
            'r10': r10,
            'r11': r11,
            'r12': r12,
            'r13': r13,
            'r14': r14,
            'r15': r15,
            'r16': r16,
            'r17': r17,
            'r18': r18,
            'r19': r19,
            'r20': r20,
            'r21': r21,
            'r22': r22,
            'r23': r23,
            'r24': r24,
            'r25': r25,
            'r26': r26,
            'r27': r27,
            'r28': r28,
            'r29': r29,
            'r30': r30})

        checkboxes_1 = widgets.HBox([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15])
        checkboxes_2 = widgets.HBox([r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30])
        # box = widgets.HBox([out, r8])

        # display(checkboxes_1, checkboxes_2)


# view = visualizaton()
# view.plot_single_bloc()
# view.interact_plot()