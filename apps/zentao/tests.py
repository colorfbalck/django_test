#-*- coding:utf-8 -*-
from django.test import TestCase

# Create your tests here.
import requests
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a1967ab3-1853-45df-abb0-de06c0b94338"
bug_data = {"msgtype": "markdown",
            "markdown": {
                "content": """<font color=\"info\">商砼平台-销售系统</font>\n
                >未解决BUG:<font color=\"warning\">12</font>\n
                >各严重等级BUG数量:
                >一级bug：<font color=\"warning\">0</font>:\n
                >二级bug：<font color=\"warning\">2</font>:\n
                 <font color=\"comment\">周震华</font>(<font color=\"warning\">2</font>)\n
                    [V-1.0.0：蜂巢APP登录首页，要求登录功能增加个防抖机制。](http://chandao.idmakers.cn/zentao/bug-view-2837.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                <font color=\"comment\">罗俊</font>(<font color=\"warning\">5</font>)\n   
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    """
                }}
data2 = {"msgtype": "markdown",
            "markdown": {
                "content": """<font color="info">19</font>

                            >未解决BUG:<font color="warning">32</font>

                            >各严重等级BUG数量:
                            >一级bug：<font color="warning">0</font>:
无
                            >二级bug：<font color="warning">2</font>:
<font color=\\"comment\\">tianye</font>(<font color=\\"warning\\">10</font>):\n[V-1.0.0：报表弹框中有数据的时候，会将关闭/确定功能键给挤出弹框。](http://chandao.idmakers.cn/zentao/bug-view-2940.html)\n[V-1.0.0：3D工厂后台设置→dcs设置界面，选择【篦冷机】页面后，无限点击节点的添加功能键会导致页面结构错乱。](http://chandao.idmakers.cn/zentao/bug-view-2946.html)\n[V-1.0.0：3D工厂后台设置→dcs设置界面，在【篦冷机】页面联系点击【添加节点】功能键，无限新增无名称节点。](http://chandao.idmakers.cn/zentao/bug-view-2947.html)\n[V-1.0.0：3D工厂后台设置→dcs设置界面，在【篦冷机】页面添加标记点弹框。标记点数量无限制。当标记点数量较大时客户端会崩溃。](http://chandao.idmakers.cn/zentao/bug-view-2948.html)\n[V-1.0.0：3D工厂，左边视频窗口点击全屏无任何反应(无遮挡)。](http://chandao.idmakers.cn/zentao/bug-view-2949.html)\n<font color=\\"comment\\">zhangfan</font>(<font color=\\"warning\\">10</font>):\n[V-1.0.0：右侧报表全屏，点击新增新增数据弹出新增数据弹框，填写好所有信息点击确定表单提交失败，报SQL错误。](http://chandao.idmakers.cn/zentao/bug-view-2927.html)\n[V-1.0.0：在右侧报表全屏界面，手动添加报表后新增报表未展示。取消全屏后报表正常展示出来。](http://chandao.idmakers.cn/zentao/bug-view-2928.html)\n[【生成大数据】生产大数据（一二线）总计21个节点共494个传感器，其中165个传感器实时数据值为0，109个历史数据值为0](http://chandao.idmakers.cn/zentao/bug-view-4390.html)\n[【视频监控】视频监控22未显示](http://chandao.idmakers.cn/zentao/bug-view-4391.html)\n[【VR视图】VR视图里面，传感器无数据时，显示实时数据空白页面](http://chandao.idmakers.cn/zentao/bug-view-4392.html)\n']
                            >三级bug：<font color="warning">0</font>:
无
                            >四级bug：<font color="warning">0</font>:
无
"""}}
res = requests.post(url=url, json=data2, verify=False).content.decode()
print(res)