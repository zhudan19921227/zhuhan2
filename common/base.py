from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 5
        self.t = 0.5
    def findElementNew(self,loca):
        try:
          ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca))
          return ele
        except:
          return ""
    def findElement(self,loca):
        try:
          ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*loca))
          return ele
        except:
          return ""

    def findElements(self, loca):
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*loca))
            return ele
        except:
            return []
    def sendKey(self,loca,text,is_clear=False):
        ele = self.findElement(loca)
        if is_clear:
            ele.clear()
        ele.send_keys(text)

    def click(self,local):
        self.findElement(local).click()
    def clear(self,local):
        self.findElement(local).clear()
    def get_text(self,local):
        try:
            t = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*local))
            r = t.text
            return r
        except:
            return ""

   # def is_display(self):
    def is_Element_Exsit(self,loc):
        try:
            self.findElement(loc)
            return True
        except:
            return False

    def isElementSExist2(self,loc):
        eles = self.findElement(loc)
        n = len(eles)
        if n == 0:
            return  False
        elif n == 1:
            return True
        else:
            return True

    def isSelected(self,local):
        try:
            r = self.findElement(local).is_selected()
            return  r
        except:
            return  False

    def is_title(self,title):
        try:
            r = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(title))
            return r
        except:
            return  False

    def is_title_contains(self,title):
        try:
            r = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(title))
            return r
        except:
            return  False

    def is_text_inElement(self,local,text):
        try:
            r = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(local,text))
            return r
        except:
            return  False
    def is_value_inElement(self,local,text):
        try:
            r = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(local,text))
            return r
        except:
            return False

    def is_alter(self):
        '''存在返回alter对象'''
        try:
            r = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return r
        except:
            return  False
    def move_to_element(self,loc):
        '''鼠标悬停'''
        try:
            element = self.findElement(loc)
        except:
            "not found element"
        else:
            ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self,loc,index=0):
        """索引选择"""
        ele = self.findElement(loc)
        Select(ele).select_by_index(index)

    def select_by_value(self,loc,value):
        '''改过Value选择'''
        ele = self.findElement(loc)
        Select(ele).select_by_value(value)

    def select_by_text(self,loc,text):
        """通过文本选择"""
        ele = self.findElement()
        Select(ele).select_by_visible_text(text)

    def js_focus_element(self,loc):
        """聚焦元素的悬停"""
        target = self.findElement(loc)
        self.driver.execute("argument[0].scrollIntoView():",target)

    def js_scroll_end(self,x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute(js)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute(js)


    def switch_handle(self,window_name):
        self.driver.switch_to.window(window_name)

    def is_exist_alter(self):
        try:
            alter=self.driver.switch_to.alert
            text=alter.text
            alter.accept()
            return  text
        except:
            return ""


'''def selectResult(self,a): #a为一组定位
     r = []
     for i in a:
          if not i.is_selected():
             i.click()
             r.append(i.is_selected())
          else:
             r.append(i.is_selected())
     return r'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.wlrc.com/")
    loc1 = (By.ID,"username")
    loc2 = (By.ID,"password")
    loc3 = (By.CSS_SELECTOR,"#form-login > button")
    loc4 = (By.CLASS_NAME,"navshow")
    ele = Base(driver)
    r1 = ele.findElement(loc1).is_displayed()
    ''' 元素是否存现在用is_displayed()'''
    print(r1)
    ele.sendKey(loc1,"13362683621")
    ele.sendKey(loc2,"zhuhan19921227")
    ele.click(loc3)
    mo = ele.findElement(loc4)
    ActionChains(driver).move_to_element(mo).perform()

    '''
    选择判断 断言  最好定位相同元素获得定位多个元素，用FOR循环
    r3=ele.selectResult(loc1)
    for i in r3:
        assert i==true    '''

    '''
    
    '''