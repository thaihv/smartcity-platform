from pywebhdfs.webhdfs import PyWebHdfsClient as h 
hdfs=h(host='tamky.xyz',port='50070',user_name='root')
ls=hdfs.list_dir('/')
print(ls)