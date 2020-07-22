# SexyImages
This can download about 1G Sexy Images from Taobao customer's album.
  1.alter 'amount' and 'loopAmount' to change number of downloads
  2.use getIP (import and set 'proxy' as proxy.random) to change proxy IP
  
Owing to the error 'Response payload is not completed', there's a lot of lost downloads, I'll be quite thankful if someone would like
help me solve this problem.






淘宝买家秀福利图
如题，爬淘宝买家秀福利图
  1.可按需更改协程数（超1000可能会报错）和单任务循环数，以下载更多，目前设置大概是下一个G
  2.可按需使用getIP更换代理IP，没被封就没必要了
  
其实理论下载数量和实际下载数量相差10倍多，（也就是目前设置本该下10多个G），但由于大量协程返回错误“Response payload is not completed”，
造成了这部分损失，目前仍未找出准确错误来源，怀疑是对方服务器的事，欢迎大佬帮忙解决
