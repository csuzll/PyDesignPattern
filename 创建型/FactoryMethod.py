"""
工厂方法模式: 分散式生产
"""

# 微信账号类
class WeChat(object):

    def send_message(self, content):
        pass

    def send_image(self, imageid):
        pass

# 微信账号A类
class AccountA(WeChat):

    def send_message(self, content):
        print("使用企业微信账号A推送信息: ", content)

    def send_image(self, imageid):
        print("使用企业微信账号A推送图片: ", imageid)

# 微信账号B类
class AccountB(WeChat):

    def send_message(self, content):
        print("使用企业微信账号B推送信息: ", content)

    def send_image(self, imageid):
        print("使用企业微信账号B推送图片: ", imageid)


# 微信账号C类（新添加产品）
class AccountC(WeChat):

    def send_message(self, content):
        print("使用企业微信账号C推送信息: ", content)

    def send_image(self, imageid):
        print("使用企业微信账号C推送图片: ", imageid)

# 工厂类（父类）
class WeChatFactory(object):

    def create_wechat(self):
        pass

# 微信账号A工厂类
class AccountAFactory(WeChatFactory):

    def create_wechat(self):
        return AccountA()

# 微信账号B工厂类
class AccountBFactory(WeChatFactory):

    def create_wechat(self):
        return AccountB()

# 微信账号C工厂类（新添加工厂）
class AccountCFactory(WeChatFactory):

    def create_wechat(self):
        return AccountC()

if __name__ == "__main__":
    # 实例化账号A
    wechat_factory_a = AccountAFactory()
    # 创建账号A的微信对象
    wechat1 = wechat_factory_a.create_wechat()
    wechat2 = wechat_factory_a.create_wechat()
    wechat3 = wechat_factory_a.create_wechat()
    # 使用账号A对象发送信息
    wechat1.send_message(content="haha")
    wechat2.send_message(content="hehe")
    wechat3.send_message(content="xixi")

    # 实例化账号B
    wechat_factory_b = AccountBFactory()
    # 创建账号B的微信对象
    wechat4 = wechat_factory_b.create_wechat()
    wechat5 = wechat_factory_b.create_wechat()
    # 使用账号B对象发送信息
    wechat4.send_message(content="heihei")
    wechat5.send_message(content="pupu")