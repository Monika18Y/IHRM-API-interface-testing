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


在postman运行时，错误解决（怀疑跨域问题导致），但出现新报错
<img width="705" alt="postman运行" src="https://github.com/user-attachments/assets/74e12ebe-6108-41c1-8858-5f045cbfbd55">
本应不通过的用例正常通过
控制参数测试对比后，发现因学习接口升级不稳定，服务端忽略了“员工id”参数

