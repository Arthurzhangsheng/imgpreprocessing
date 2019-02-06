import png

def insert_text_chunk(src_png, dst_png, text):
    '''在png中的第二个chunk插入自定义内容'''
    reader = png.Reader(filename=src_png)
    chunks = reader.chunks()#创建一个每次返回一个chunk的生成器
    chunk_list = list(chunks)#把生成器的所有元素变成list
    print(f"target png total chunks number is {len(chunk_list)}")
    chunk_item = tuple([b'tEXt', text])

    #第一个chunk是固定的IHDR，我们把tEXt放在第2个chunk
    index = 1
    chunk_list.insert(index, chunk_item)

    with open(dst_png, 'wb') as dst_file:
        png.write_chunks(dst_file, chunk_list)

def read_text_chunk(src_png, index=1):
    '''读取并打印png的第N个chunk'''
    reader = png.Reader(filename=src_png)
    chunks = reader.chunks()
    chunk_list = list(chunks)   
    print(f"target png total chunks number is {len(chunk_list)}")
    print(chunk_list[index])


if __name__ == '__main__':
    #---------以下是需要修改的部分-------------
    src_png = r'C:\Users\Administrator\Desktop\00001.png'   
    dst_png = r'C:\Users\Administrator\Desktop\result.png'
    text = b'just for test'
    #-----------以上是可修改的部分----------------
    insert_text_chunk(src_png, dst_png, text)
    read_text_chunk(dst_png)