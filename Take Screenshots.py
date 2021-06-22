#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui


# In[ ]:


def add_al_screenshots():
    x = 0
    while x < 360:
        time.sleep(5)
        pyautogui.screenshot('USAl_' + (day.today().year + day.today().month + day.today().day) + '-' + str(x) + '.png')
        x += 1

