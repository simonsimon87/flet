from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
   BG = '#041955'
   FWG = '#97b4ff'
   FG = '#3450a1'
   PINK = '#eb06ff'
   
   circle = Stack(
      controls=[
         Container(
            width=100,
            height=100,
            border_radius=50,
            bgcolor='white12',
         ),
         Container(
            gradient=SweepGradient(
               center=alignment.center,
               start_angle=0.0,
               end_angle=3,
               stops=[0.5,0.5],
               colors=['#00000000', PINK]
            ),
            width=100,
            height=100,
            border_radius=50,
            content=Row(
               alignment='center',
               
            )
         )
      ]
   )
   
   def shrink(e):
      page_2.controls[0].width = 120
      page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
      page_2.controls[0].border_radius = border_radius.only(
         top_left=25,
         top_right=0,
         bottom_left=25,
         bottom_right=0,
      )
      page_2.update()
      
   def restore(e):
      page_2.controls[0].width = 400
      page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
      page_2.update()
   
   
   create_task_view = Container(
      content=Container(
         on_click= lambda _:page.go('/'),
         height=40,
         width=40,
         content=Text('x')
         
      )
   )
   
   tasks=Column(
      height=300,
      scroll='auto',
      controls=[
         #Container(height=50, width=300, bgcolor='red'),
         #Container(height=50, width=300, bgcolor='red'),
         #Container(height=50, width=300, bgcolor='red'),
         #Container(height=50, width=300, bgcolor='red'),
      ]
   )
   
   for i in range(10):
      tasks.controls.append(
         Container(height=70, width=400, bgcolor=BG, border_radius=20,
                   padding=padding.only(left=20, top=25),
                   content=CustomCheckBox(
                      PINK,
                      size=20,
                      font_size=20,
                      label='create interstiong content'))
         
      )
   
   categories_card = Row(
      scroll='auto',
   )
   
   categories = ['busniss', 'family', 'friends']
   for i, category in enumerate(categories):
      categories_card.controls.append(
         Container(
            bgcolor=BG,
            height=110,
            width=170,
            border_radius=20,
            padding=15,
            content=Column(
               controls=[
                  Text('40 tasks'),
                  Text('category'),
                  Container(
                     width=160,
                     height=5,
                     bgcolor='white12',
                     border_radius=20,
                     padding=padding.only(right=i*20),
                     content=Container(
                        bgcolor=PINK,
                     )
                     
                  )
               ]
            )
         )
      )
   
   first_page_contents = Container(
      content=Column(
         controls=[
            Row(alignment='spaceBetween',
               controls=[
                  Container(on_click=lambda e: shrink(e),
                     content=Icon(
                        icons.MENU
                     )
                  ),
                  Row(
                     controls=[
                        Icon(icons.SEARCH),
                        Icon(icons.NOTIFICATIONS_OUTLINED)
                     ]
                  )
               ]
            )
            ,
            Container(height=20),
            Text(
               value='How Are you Mido',
            ),
            Text(
               value='CATEGORIES',
            ),
            Container(
               padding=padding.only(
                  top=10, bottom=20
               ),
               content=categories_card
            ),
            Container(height=20),
            Text('today\' tasks'),
            Stack(
               controls=[
                  tasks,
                  FloatingActionButton(bottom=2,right=5,
                     icon= icons.ADD, on_click=lambda _:page.go('/create_task')
                  ),
               ]
            )
            
         ]
      )
   )
   page_1 = Container(
      width=400,
      height=850,
      bgcolor=BG,
      border_radius=20,
      padding=padding.only(left=50, top=60, right=200),
      content=Column(
         controls=[
            Row(alignment='end',
               controls=[
            Container(border_radius=25,padding=padding.only(top=13,left=15),height=50,width=50,border=border.all(color='white', width=1),
            on_click=lambda e: restore(e),
               content=Text('<'),
            )
         ]
            ),
            Container(height=20),
            circle,
            Text('Ben Slilih Madani', size=25, color='white')
         ]
      )
   )
   page_2 = Row(alignment='end',
      controls=[
         Container(
            width=400, 
            height=850, 
            bgcolor=FG, 
            border_radius=25,
            animate=animation.Animation(600, AnimationCurve.EASE_IN_CUBIC),
            animate_scale=animation.Animation(400, curve='decelerate'),
            padding=padding.only(
               left=20, 
               top=50, 
               right=20, 
               bottom=5
            ),
            content=Column(
               controls=[
                  first_page_contents
               ]
            )
         )
      ]
   )
   
   container = Container(
      width=400, 
      height=850, 
      bgcolor=BG, 
      border_radius=25,
      content=Stack(
         controls=[
            page_1,
            page_2
         ]
      )
   )
   
   pages = {
      '/':View(
         "/",
         [
            container
         ]
      ),
      '/create_task':View(
         "/crate_task",
         [
            create_task_view
         ]
      )
   }
   
   def route_change(route):
      page.views.clear()
      page.views.append(
         pages[page.route]
      )
   
   page.add(container)
   page.theme_mode = 'dark'
   page.on_route_change = route_change
   page.go(page.route)


app(target=main)