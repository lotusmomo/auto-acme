# Auto ACME - Automatic Certificate Issuance with Github Actions and acme.sh

> Note that the following English version is translated by ChatGPT, please read Chinese version if possible.

## Use Case

`acme.sh` is a tool implemented purely in Shell, which can automatically apply for SSL certificates through the acme protocol, and it has automatic renewal function, which is very convenient. However, in mainland China, due to the blocking of the Great Firewall of China, it is not possible to stably connect to Letsencrypt's servers, resulting in certificate application failures. This project uses Github Actions to obtain certificates, packages them, and uploads them to artifacts. Clients can use a Python script to periodically download the certificates to solve such problems.

## Usage

Fork this project and set it as a private repository, unless you want everyone to be able to access your certificate private key.

Add necessary parameters to Variables:

- `SERVER`: The CA (Certificate Authority) you want to choose.

  acme.sh provides these CAs for you to choose from: https://github.com/acmesh-official/acme.sh/wiki/Server. Fill in one of them, recommended options are `letsencrypt` or `zerossl`.

- `DNS`: Your domain's DNS resolution service provider.

  For example, if you are using Cloudflare as your resolution service, enter `dns_cf`.

- `DOMAINS`: The domain(s) for which you want to apply for certificates. Separate them with spaces, like this:

  ```
  example1.com example2.net example3.io
  ```

The following should be added to Secrets:

- `EMAIL`: Your email, used for registration with the CA.

- `DNSAPI`: The token for your domain service provider, in the following format:

  ```shell
  DP_Id="xxxxx"
  DP_Key="xxxxxxxxxxxxxxxxxx"
  ```


Actions will be executed every Sunday at midnight UTC to ensure that the certificates are up to date.

## Deploying Certificates

Use the `getcert.py` script provided in the project. You can fill in the following parameters at the beginning of the file:

```python
OWNER     = ""
REPO      = ""
GH_TOKEN  = ""
CERT_PATH = ""
```

- `OWNER` is the owner of the repository, usually your own username.
- `REPO` is the name of the repository. After you fork it, you can change the repository name under your account. In most cases, it will be the same as this repository.
- `GH_TOKEN` is your Github Token.
- `CERT_PATH` is the path where the certificates will be saved.

Alternatively, it can accept these parameters from the command line.

# 使用 Github Actions 与 acme.sh 自动签发证书

## 使用场景

`acme.sh`是一个纯Shell实现的工具，可以透过acme协议自动申请SSL证书，而且有自动续约功能，十分方便。但是在中国大陆地区，由于互联网防火长城的封锁，不能稳定的连接到Letsencrypt的服务器而导致证书申请失败。本项目通过使用 Github Actions 获取证书，将证书打包后上传到 artifact ，客户端使用python脚本定期下载来解决此类问题。

## 使用方法

Fork本项目并设置为私密仓库，除非你想让所有人都能获取你的证书私钥。

添加一些必要的参数到到Variables：

- `SERVER`：你要选择的CA。

  acme.sh提供了这些CA供你选择：https://github.com/acmesh-official/acme.sh/wiki/Server。填入其中之一即可，推荐 `letsencrypt` 或 `zerossl`。

- `DNS`：你的域名dns解析服务提供商。

  比如你的解析服务用的是Cloudflare，则填入 `dns_cf`。

- `DOMAINS`：欲申请证书的域名。用空格隔开，形如

  ```
  example1.com example2.net example3.io
  ```

下面这些添加到Secrets：

- `EMAIL`：你的邮件，用于在CA注册。

- `DNSAPI`：记录域名服务商的token，形如

  ```shell
  DP_Id="xxxxx"
  DP_Key="xxxxxxxxxxxxxxxxxx"
  ```


Actions将在世界协调时的每周日零点执行一次，以确保证书是最新的。

## 部署证书

使用项目内的`getcert.py`。你可以在文件的开头填入这些参数：

```python
OWNER     = ""
REPO      = ""
GH_TOKEN  = ""
CERT_PATH = ""
```

- `OWNER`是仓库的拥有者，通常是你自己的用户名称。
- `REPO`是仓库的名称，在你复刻之后你可以更改你名下的仓库名称，一般情况下，与本仓库一致。
- `GH_TOKEN`你的Github Token。
- `CERT_PATH`证书的保存路径。

亦可从命令行接受参数。
