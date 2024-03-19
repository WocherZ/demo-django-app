import ipywidgets as widgets  # pip install ipywidgets jupyter nbextension enable widgetsnbextension
# from IPython.display import display
# from IPython.display import HTML
import schemdraw  # !/usr/local/bin/python3 -m pip install SchemDraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')


class visualizaton:
    def __init__(self) -> None:
        pass

    def plot_scheme(self, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20,
                    r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35, r36):
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

        with schemdraw.Drawing(show=True) as d:
            import matplotlib
            matplotlib.use('Agg')  # Set the backend here

            d = schemdraw.Drawing()
            d.config(unit=3)

            d += elm.SourceV().down().label('12V\n10A\n№1')
            d += elm.Line().down()

            d += (rel1 := elm.compound.Relay(unit=2, link=r1, switch='spdt', label='1')).right().anchor('a')
            d += (line1 := elm.Line()).down(d.unit * 4).at(rel1.b).dot()

            d += (JP1 := elm.Header(cols=6, rows=2, shownumber=False, pinsright=['+', '-'],
                                    pinalignright='center').anchor('pin3'))
            d += (line2 := elm.Line()).right().at(rel1.c)
            d += (JP2 := elm.Header(cols=1, rows=4, shownumber=False, pinalignright='center').anchor('pin1'))

            d += elm.Line().right().at(JP2.pin2)
            d += elm.Line().up(d.unit * 0.2)
            d += (rel2 := elm.compound.Relay(unit=2, link=r1, switch='spdt', label='2')).right().anchor('c')
            d += elm.Line().up().at(rel2.a)
            d += elm.SourceV().up(d.unit * 1.13).label('12V\n10A\n№1').reverse()

            d += elm.Line().down(d.unit * 4).at(rel2.b).dot()
            d += (JP3 := elm.Header(cols=6, rows=2, shownumber=False, pinsright=['+', '-'],
                                    pinalignright='center').anchor('pin4'))

            # 2
            d += elm.Line().down(d.unit * 2.63).at(JP3.pin8)
            d += elm.Line().left(d.unit * 0.2).at(JP3.pin1)
            d += elm.Line().down(d.unit * 1.8)

            d += (rel21 := elm.compound.Relay(unit=2, link=r12, switch='spst', label='21')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel21.b)
            d += elm.Line().right(d.unit * 0.4)

            d += elm.Line().down(d.unit * 2.63).at(JP3.pin11)
            d += elm.Line().right(d.unit * 0.3).at(JP3.pin6)
            d += elm.Line().down(d.unit * 1.8)

            d += (rel27 := elm.compound.Relay(unit=2, link=r18, switch='spst', label='27')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel27.b)
            d += elm.Line().left(d.unit * 0.5)

            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')

            d += elm.Line().left(d.unit * 0.5).at(JP2.pin3)
            d += elm.Line().down(d.unit * 0.5)
            d += elm.Line().right(d.unit)
            d += elm.Line().down(d.unit * 0.1)
            d += (rel4 := elm.compound.Relay(unit=2, link=r1, switch='spst', label='4')).right().anchor('a')

            # move to rel 9-12
            d += elm.Line().right(d.unit * 1.5).at(rel4.b)
            d += elm.Line().down(d.unit * 0.1)
            d += (rel9 := elm.compound.Relay(unit=2, link=r3, switch='spdt', label='9')).right().anchor('a')
            d += elm.Line().at(rel9.b).down(d.unit * 0.1)
            d += elm.Line().left(d.unit * 1.05)
            d += elm.Line().to(JP3.pin3)

            d += elm.Line().down(d.unit * 0.3).at(rel9.c)
            d += (rel11 := elm.compound.Relay(unit=2, link=r3, switch='spst', label='11')).right().anchor('a')
            d += elm.Line().at(rel11.b).down(d.unit * 0.1)
            d += elm.Line().left(d.unit * 0.4)
            d += elm.Line().to(JP3.pin5)

            d += elm.Line().right(d.unit * 0.8).at(JP3.pin12)
            d += elm.Line().down(d.unit * 3)
            d += elm.Line().left(d.unit * 5)
            d += elm.Line().up(d.unit * 10)
            d += elm.Line().right(d.unit * 3.69)

            d.push()  # loop to 3

            d += elm.Line().right(d.unit).at(JP2.pin4)
            d += elm.Line().down(d.unit * 1.4)
            d += elm.Line().left(d.unit)
            d += elm.Line().down(d.unit * 0.1)
            d += (rel3 := elm.compound.Relay(unit=2, link=r1, switch='spst', label='3')).right().anchor('a')
            d += elm.Line().at(rel3.b).down(d.unit * 0.1)
            d += elm.Line().left(d.unit * 0.53)
            d += elm.Line().to(JP1.pin4)

            # 1
            d += elm.Line().down(d.unit * 1.43).at(JP1.pin8)
            d += elm.Line().left(d.unit * 0.2).at(JP1.pin1)
            d += elm.Line().down(d.unit * 0.6)

            d += (rel13 := elm.compound.Relay(unit=2, link=r4, switch='spst', label='13')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel13.b)
            d += elm.Line().right(d.unit * 0.4)

            d += elm.Line().down(d.unit * 1.43).at(JP1.pin11)
            d += elm.Line().right(d.unit * 0.3).at(JP1.pin6)
            d += elm.Line().down(d.unit * 0.6)

            d += (rel20 := elm.compound.Relay(unit=2, link=r11, switch='spst', label='20')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel20.b)
            d += elm.Line().left(d.unit * 0.5)

            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')

            d += elm.Line().left(d.unit * 1).at(JP1.pin7)
            d += elm.Line().up(d.unit * 6.88)
            d += elm.Line().right(d.unit * 1.27)

            d.pop()
            # к 3
            d += elm.Line().right(d.unit * 2.7).color('white')
            d += elm.Line().down(d.unit * 0.1)
            d += elm.SourceV().down().label('12V\n10A\n№3')
            d += elm.Line().down()

            d += (rel5 := elm.compound.Relay(unit=2, link=r2, switch='spdt', label='5')).right().anchor('a')
            d += (line1 := elm.Line()).down(d.unit * 4).at(rel5.b).dot()

            d += (JP4 := elm.Header(cols=6, rows=2, shownumber=False, pinsright=['+', '-'],
                                    pinalignright='center').anchor('pin3'))
            d += (line2 := elm.Line()).right().at(rel5.c)
            d += (JP5 := elm.Header(cols=1, rows=4, shownumber=False, pinalignright='center').anchor('pin1'))

            d += elm.Line().right().at(JP5.pin2)
            d += elm.Line().up(d.unit * 0.2)
            d += (rel6 := elm.compound.Relay(unit=2, link=r2, switch='spdt', label='6')).right().anchor('c')
            d += elm.Line().up().at(rel6.a)
            d += elm.SourceV().up(d.unit * 1.13).label('12V\n10A\n№4').reverse()

            d += elm.Line().down(d.unit * 4).at(rel6.b).dot()
            d += (JP6 := elm.Header(cols=6, rows=2, shownumber=False, pinsright=['+', '-'],
                                    pinalignright='center').anchor('pin4'))

            # 4
            d += elm.Line().down(d.unit * 2.63).at(JP6.pin8)
            d += elm.Line().left(d.unit * 0.2).at(JP6.pin1)
            d += elm.Line().down(d.unit * 1.8)

            d += (rel36 := elm.compound.Relay(unit=2, link=r27, switch='spst', label='36')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel36.b)
            d += elm.Line().right(d.unit * 0.4)

            d += elm.Line().down(d.unit * 2.63).at(JP6.pin11)
            d += elm.Line().right(d.unit * 0.3).at(JP6.pin6)
            d += elm.Line().down(d.unit * 1.8)

            d += (rel42 := elm.compound.Relay(unit=2, link=r33, switch='spst', label='42')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel42.b)
            d += elm.Line().left(d.unit * 0.5)

            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')

            d += elm.Line().left(d.unit * 0.5).at(JP5.pin3)
            d += elm.Line().down(d.unit * 0.5)
            d += elm.Line().right(d.unit)
            d += elm.Line().down(d.unit * 0.1)
            d += (rel8 := elm.compound.Relay(unit=2, link=r2, switch='spst', label='8')).right().anchor('a')
            d += elm.Line().at(rel8.b).down(d.unit * 0.1)
            d += elm.Line().right(d.unit * 0.35)
            d += elm.Line().to(JP6.pin2)

            d += elm.Line().right(d.unit * 0.8).at(JP3.pin12)
            d += elm.Line().down(d.unit * 3)
            d += elm.Line().left(d.unit * 5)
            d += elm.Line().up(d.unit * 10)
            d += elm.Line().right(d.unit * 3.69)

            d.push()  # loop to 3

            d += elm.Line().right(d.unit).at(JP5.pin4)
            d += elm.Line().down(d.unit * 1.4)
            d += elm.Line().left(d.unit)
            d += elm.Line().down(d.unit * 0.1)
            d += (rel7 := elm.compound.Relay(unit=2, link=r2, switch='spst', label='7')).right().anchor('a')
            d += elm.Line().at(rel7.b).down(d.unit * 0.1)
            d += elm.Line().left(d.unit * 0.9)
            d += elm.Line().up(d.unit * 1.17)
            d += elm.Line().left(d.unit * 0.8)
            d += elm.Line().down(d.unit * 0.1)
            d += (rel10 := elm.compound.Relay(unit=2, link=r3, switch='spdt', label='10')).right().anchor('a')
            d += elm.Line().right(d.unit * 0.6).at(rel10.b)
            d += elm.Line().to(JP4.pin2)

            d += elm.Line().down(d.unit * 0.3).at(rel10.c)
            d += (rel12 := elm.compound.Relay(unit=2, link=r3, switch='spst', label='12')).right().anchor('a')
            d += elm.Line().at(rel12.b).down(d.unit * 0.1)
            d += elm.Line().right(d.unit * 1.3)
            d += elm.Line().down(d.unit * 0.1).to(JP4.pin4)

            # .to(JP4.pin4)

            # 3
            d += elm.Line().down(d.unit * 1.43).at(JP4.pin8)
            d += elm.Line().left(d.unit * 0.2).at(JP4.pin1)
            d += elm.Line().down(d.unit * 0.6)

            d += (rel28 := elm.compound.Relay(unit=2, link=r19, switch='spst', label='28')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel28.b)
            d += elm.Line().right(d.unit * 0.4)

            d += elm.Line().down(d.unit * 1.43).at(JP4.pin11)
            d += elm.Line().right(d.unit * 0.3).at(JP4.pin6)
            d += elm.Line().down(d.unit * 0.6)

            d += (rel35 := elm.compound.Relay(unit=2, link=r26, switch='spst', label='35')).right().anchor('a')
            d += elm.ElementDrawing(heat).down().at(rel35.b)
            d += elm.Line().left(d.unit * 0.5)

            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')
            d += elm.Line().left(d.unit * 0.05).color('white')
            d += elm.Line().left(d.unit * 0.05).color('black')

            d += elm.Line().right(d.unit * 1).at(JP6.pin12)
            d += elm.Line().up(d.unit * 7)
            d += elm.Line().left(d.unit * 1.53)

            d += elm.Line().left(d.unit * 0.8).at(JP4.pin7)
            d += elm.Line().down(d.unit * 3)
            d += elm.Line().right(d.unit * 5)
            d += elm.Line().up(d.unit * 10.1)
            d += elm.Line().left(d.unit * 3.933)
            d += elm.Line().down(d.unit * 0.2)

            # d.draw()
            d.save('static/img/scheme.svg')
            print('Image saved successfully')


# view = visualizaton()

# ar - массив значений реле
# Андрей! Три строки ниже удадляешь и передаешь массив с реле сразу в функцию
# ar = []
# for _ in range(36):
#     ar.append(True)
#
# view.plot_scheme(*ar)
# SVG('city.svg')