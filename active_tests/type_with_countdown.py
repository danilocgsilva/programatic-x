from programatic_x.LongType import LongType
from time import sleep

long_type = LongType()
sleep(3)

text_with_specials = r'''Non-English: 哈あµø∫

Overview of Owls
Owls belong to the order Strigiformes, which comprises over 200 species divided into two main families:
Tytonidae (barn owls) and Strigidae (true owls).
They are found on every continent except Antarctica, thriving in diverse habitats, from dense forests to open grasslands and urban areas.

        .-"""""""-.    .'""."".""`.
       /   \ * /   \  /  ^ \   /^  \
      { ((@)\*/((@) }.{ ~Q '\ / Q ~}}
     ( `.~~ .V. ~~.'}.`._.'  V`._.'  )
     ( ( `-')  `-'  }   ~~     ~~    )
     (  (   ) ^ ^   0 "  " "   (  (   )
     (      )  ^^  00   "      (      .)
     ( (   )     ^ 00     "    ( (   ) )
      {   )  ^^   .0'0  "   "   (     }
       { }  ^   ))    0          (   }
        `--叩w叩--'       "--叩m叩------ "

By the way, the fancy character comes from the following stackoverflow link: https://stackoverflow.com/questions/75051207/pyautogui-write-not-automatically-using-shift-to-type-characters-on-non-englis/79134597\#79134597
'''

long_type.type(text_with_specials)
