class Solution:
    
    
    def calculate_seat_avail(self,a,i,capacity,drop_dict):
            if i==0:
                global starting_point
                global passengers_in
                global end_point
                starting_point=a[1]
                passengers_in=a[0]
                end_point=a[2]
                drop_dict[a[2]]=a[0]
                return True
            if a[1] >end_point:
                seat_available=capacity-drop_dict[end_point]
                if a[0]> seat_available:
                    return False
                else:
                    starting_point=a[1]
                    passengers_in=a[0]
                    end_point=max(end_point,a[2])
                    if a[2] in drop_dict:
                        drop_dict[a[2]]=drop_dict[a[2]]+a[0]
                    else:   
                        drop_dict[a[2]]=a[0]
                    return True
            if a[1]<=end_point:
                temp=[]
                total=0
                list_of_droping_points=drop_dict.keys()
                if a[1] in drop_dict or a[1]<max(list_of_droping_points):
                    list_of_keys=[k for k,v in drop_dict.items() if k<=a[1]]
                    for k,v in drop_dict.items():
                        for i in list_of_keys:
                            if k==i:
                                temp.append(i)
                                total=total+v
                    seat_available=capacity-(passengers_in-total)
                    [drop_dict.pop(key) for key in temp]
                    
                    passengers_in=passengers_in-total
                else:
                    seat_available=capacity-passengers_in
                        
                if a[0]>seat_available:
                    return False
                else:
                    starting_point=a[1]
                    passengers_in=passengers_in+a[0]
                    end_point=max(end_point,a[2])
                    if a[2] in drop_dict:
                        drop_dict[a[2]]=drop_dict[a[2]]+a[0]
                    else:   
                        drop_dict[a[2]]=a[0]
                    return True
    
    
    def carPooling(self, trips, capacity: int) -> bool:
        tripsorted=sorted(trips,key=lambda x:x[1])
        drop_dict={}
        count=0
        for i in range(0,len(tripsorted)):
            if self.calculate_seat_avail(tripsorted[i],i,capacity,drop_dict):
                count=count+1
            else:
                return False
        if count==len(tripsorted):
            return True
        
s= Solution()
trips=[[2,1,5],[3,3,7]]
capacity=4
print(s.carPooling(trips,capacity))        