import csv

def formatItem(item):
    if item.isnumeric():
        item_last_index = len(item)
        item_last_three_digits = item[item_last_index -3:item_last_index]
        if item_last_three_digits == '000':
            item = item.zfill(10)
        else:
            item = item + '000'
            item = item.zfill(10)
    
    return item

with open(path_to_file_in) as f_in:
    data = f_in.readlines()
    #data = '123,2-234000,ABXD234234,23000'
    
    with open(path_to_file_out, 'a') as f_out:
        f_out_writer = csv.writer(f_out)
    
        item_list = data.split(',')
        
        for item in item_list:
            hifen_position = item.find('-')
            if hifen_position == -1:
                item = formatItem(item)
                item = '1-' + item
                f_out_writer.writerow([item])
                
            else:
                splitted_item = item.split('-')
                splitted_item[1] = formatItem(splitted_item[1])
                item = splitted_item[0] + '-' + splitted_item[1]
                f_out_writer.writerow([item])
