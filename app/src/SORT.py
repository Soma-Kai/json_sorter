class Sort:
    def __init__(self,calc_type,data):
        self.type = calc_type
        self.data = data
        self.length_data = len(data)

    def make_id_array(self):
        self.index_array = [ i for i in range(self.length_data) ] 
        self.id_array = []
        for i in self.index_array:
            self.id_array.append(self.data[i]["id"])

    def calc(self):
        self.make_id_array()
        if self.type == "insertion":
            self.insert_sort()

        if self.type == "quick":
            self.id_array, self.index_array = self.quick_sort(self.id_array,self.index_array)

        if self.type == "merge":
            self.merge_sort(self.id_array, self.index_array, 0, self.length_data - 1)



    def insert_sort(self):
        for i in range(1, self.length_data):
            j = i - 1
            ele = self.id_array[i]
            ele_index = self.index_array[i]
            while self.id_array[j] > ele and j >= 0:
                self.id_array[j + 1] = self.id_array[j]
                self.index_array[j+1] = self.index_array[j]
                j -= 1
            self.id_array[j + 1] = ele
            self.index_array[j + 1] = ele_index



    def quick_sort(self,arr,arr_id):
        left = []
        left_id = []
        right = []
        right_id = []
        if len(arr) <= 1:
            return arr, arr_id

        ref = arr[0]

        if len(arr) == 2:
            if arr[1] < ref:
                left.append(arr[1])
                left_id.append(arr_id[1])
                right.append(ref)
                right_id.append(arr_id[0])
            else:
                left.append(ref)
                left_id.append(arr_id[0])
                right.append(arr[1])
                right_id.append(arr_id[1])

        else:
            for index,ele in enumerate(arr):
                if ele < ref:
                    left.append(ele)
                    left_id.append(arr_id[index])
                elif ele >= ref:
                    right.append(ele)
                    right_id.append(arr_id[index])
        left, left_id = self.quick_sort(left,left_id)
        right, right_id = self.quick_sort(right,right_id)
        left.extend(right)
        left_id.extend(right_id)
        return left, left_id



    def merge(self,arr,arr_id, start, mid, end):
        data_temp = []
        data_temp_id = []
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                data_temp.append(arr[i])
                data_temp_id.append(arr_id[i])
                i = i + 1
            else:
                data_temp.append(arr[j])
                data_temp_id.append(arr_id[j])
                j = j + 1

        while i <= mid:
            data_temp.append(arr[i])
            data_temp_id.append(arr_id[i])
            i = i + 1

        while j <= end:
            data_temp.append(arr[j])
            data_temp_id.append(arr_id[j])
            j = j + 1

        k = start
        for val in data_temp:
            arr[k] = val
            k = k + 1  

        k = start
        for json_id in data_temp_id:
            arr_id[k] = json_id
            k = k + 1  

    def merge_sort(self, arr, arr_id, start, end):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.merge_sort(arr, arr_id, start, mid)
        self.merge_sort(arr, arr_id, mid + 1, end)
        self.merge(arr, arr_id, start, mid, end)











