# coding:utf-8
import msgpack

# f = open("C:\Users\chen\Desktop\data.txt", "r")
# lines = f.readlines()
# if not lines:
#     print 'hhh'
# print type(lines)
# line_data = []
# rs2freq = {}
# print len(lines)
# for i in range(len(lines)):
#     line_data.append(lines[i].split())
#     rs2freq[line_data[i][0]] = line_data[i][1:]
# print line_data
# print rs2freq

gnesfp = open("C:\Users\chen\Desktop\\6211.bson", "r")
gene_nm_exons = msgpack.unpackb(gnesfp.read())
print gene_nm_exons
print type(gene_nm_exons)



