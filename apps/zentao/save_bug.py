# -*- coding: utf-8 -*-
# @Time    : 2022-05-24 15:38
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : get_bug.py 
# @Software: PyCharm
import json
import requests


class GetBugList:

    def __init__(self, zentaosid):
        self.res = requests
        self.zentaosid = zentaosid

    def bug_list(self, projectid, bugtype):
        """
        通过项目ID，所需类型bug
        :param projectid: 项目ID
        :param bugtype: BUG类型
        :return:
        """
        url = "http://chandao.idmakers.cn/zentao/bug-browse-{}-0-{}-0--0-1000-1.json?zentaosid={}".\
            format(projectid, bugtype, self.zentaosid,)
        heder = {
            'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
            'cache-control': "no-cache",
        }
        result = self.res.get(url=url, headers=heder).content.decode('utf-8')
        if "<html>" not in result:
            results = json.loads(result)
            content = json.loads(results["data"])
            return content
        else:
            print("查询失败:{}".format(result))
            raise

    def get_bug_list(self, projectid):
        """
        通过项目id查询未关闭，未解决的BUG数量
        :param projectid:
        :return:
        """
        bugtype = ["unresolved", "toclosed"]
        project_name = None
        bugs = []
        for i in range(len(bugtype)):
            data = self.bug_list(projectid, bugtype[i])
            if data:
                project_name = str(data["title"]).replace('::Bug', "")
                total_bug = len(data["bugs"])
                bugs.append(total_bug)
            bugs.append(project_name)
        return bugs

    def get_all_prodcuts(self):
        """查询所有项目id"""
        data = self.bug_list(0, "all")
        product = data["products"]
        products = []
        for k, v in product.items():
            product = k
            products.append(product)
        return products

    def add_bug(self, projectid):
        """添加bugs到数据库"""
        projects = self.get_all_prodcuts()
        for project in projects:
            self.add_bug(project)

    def add_all_bug(self):
        """
        查询所有bug
        :return:
        """
        prodcuts = self.get_all_prodcuts()
        all_bug = []
        for prodcut in prodcuts:
            bugs = self.bug_list(prodcut, 'unresolved')["bugs"]
            if len(bugs) > 0:
                for i in range(len(bugs)):
                    bug = bugs[i]
                    all_bug.append(bug)
        return all_bug


if __name__ == '__main__':
    test = "rdroduvh3g89bk8943eta11hv6"
    res = GetBugList(test)
    # result = res.get_bug_list(48)
    # print(result)
    # results = res.get_all_prodcuts()
    bug_list = res.add_all_bug()
    print(bug_list)



