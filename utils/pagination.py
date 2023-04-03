# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 21:34
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : pagination.py
# @Software: PyCharm
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    # 默认情况下，每一页显示条数为2
    page_size = 2
    # 指定前端能分页的最大Page_size
    page_size_query_param = 's'
    max_page_size = 50

    def get_paginated_response(self, data):
        response = super(PageNumberPaginationManual, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data['current_page_num'] = self.page.number
        return response