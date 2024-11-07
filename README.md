# IHRM-API-interface-testing
IHRM项目**接口测试**


# 工具
Postman、newman拓展库


# 测试内容
根据接口文档对接口增删改查以及常见场景测试


# 测试遇到的问题
使用newman-reporter-htmlextra生成测试报告时，发现大量断言不通过
![测试报告报错](https://github.com/user-attachments/assets/eba4b1c9-86c0-4fc1-8f4a-32b5eeca41cd)
返回状态码401，疑似token过期或丢失
