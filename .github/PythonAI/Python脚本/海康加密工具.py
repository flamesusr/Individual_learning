# 导入必要的库
from collections import OrderedDict  # 有序字典，用于保持请求头的顺序
import hmac  # 用于HMAC加密算法
import hashlib  # 提供多种安全哈希算法
import base64  # 用于Base64编码
#import time

# ===================== 全局配置参数 =====================
# 注意：以下参数需要从海康开放平台获取，请确保与平台配置完全一致
URL = "/artemis/api/nms/v1/online/pms/device/get"  # 请求的API接口路径
appKey = "23003292"  # 应用唯一标识（类似账号）
appSecret = "huYd9V9zPd3aNlyc8CDN"  # 应用密钥（类似密码，需严格保密）
x_ca_signature_headers = "x-ca-key"  # 指定参与签名的请求头字段


# ===================== 签名工具类 =====================
class SignUtil:
    @staticmethod
    def sign(method, url, headers, app_secret):
        """
        生成海康API请求签名
        参数说明：
        method: HTTP请求方法（大写字母），例如：POST
        url: 请求的API路径，例如：/artemis/api/...
        headers: 包含请求头的字典
        app_secret: 应用密钥（用于加密的关键参数）
        """
        # 步骤1：构建待签名字符串（这是签名的核心内容）
        string_to_sign = (
            f"{method}\n"  # HTTP方法（例如：POST）
            f"{headers['Accept']}\n"  # 接受的数据类型（例如：*/* 表示接受所有类型）
            f"{headers['Content-Type']}\n"  # 发送的内容类型（例如：application/json）
            f"x-ca-key:{headers['X-Ca-Key']}\n"  # 强制小写的关键头（注意冒号后的值）
            # f"x-ca-timestamp:{headers['X-Ca-Timestamp']}\n"  # 时间戳（正式使用需要取消注释）
            f"{url}"  # API请求路径（注意最后没有换行符）
        )

        # 步骤2：将字符串转换为字节流（加密函数需要字节类型数据）
        byte_stream = string_to_sign.encode("utf-8")  # 必须使用UTF-8编码

        # 调试输出（开发时可查看签名内容）
        print("【待签名字符串】")
        print(repr(string_to_sign))  # 显示原始字符串（包含换行符）
        print(f"字节长度: {len(byte_stream)} ")  # 打印字节长度用于校验
        print("字节内容:", byte_stream)  # 显示实际参与加密的字节数据

        # 步骤3：使用HMAC-SHA256算法生成签名
        digest = hmac.new(
            app_secret.encode("utf-8"),  # 将密钥转换为字节
            byte_stream,  # 待签名字节流
            hashlib.sha256  # 指定哈希算法
        ).digest()  # 生成二进制签名

        # 步骤4：将二进制签名转换为Base64字符串
        return base64.b64encode(digest).decode()  # 解码为字符串格式


# ===================== 主函数（使用示例） =====================
def main():
    # 设置请求头（注意顺序可能影响签名）
    headers = OrderedDict()  # 使用有序字典保证字段顺序
    headers["Accept"] = "*/*"  # 客户端接受的数据类型
    headers["Content-Type"] = "application/json"  # 发送JSON格式数据
    headers["x-ca-signature-headers"] = x_ca_signature_headers  # 指定签名头
    headers["X-Ca-Key"] = appKey  # 应用标识
    #headers["X-Ca-Timestamp"] = "1744765000401"  # 测试用固定时间戳（生产环境需动态生成）

    # 生成签名
    sign_result = SignUtil.sign(
        method="POST",  # 请求方法
        url=URL,  # API路径
        headers=headers,  # 请求头字典
        app_secret=appSecret  # 应用密钥（重要！）
    )

    # 输出结果
    print(f"【实际签名】\n{sign_result}")


# 程序入口
if __name__ == "__main__":
    main()
