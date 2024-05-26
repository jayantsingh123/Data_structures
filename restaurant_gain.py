def add_seated(seated,id):
    pass

def remove_seated(seated, id):
    pass

def add_waitlist(waitlist, id):
    pass


def remove_waitlist(waitlist, id):
    pass
def main_fn(seats_avail, paying_guests, guest_movement):
    seated, waitlist, eat = set(),[],[0]*len(paying_guests)
    for i in range(len(guest_movement)):
        if eat[guest_movement[i]]==0:
            # if seats are available
            if seats_avail>0:
                seated.add(guest_movement[i])
                eat[guest_movement[i]]=1
                seats_avail-=1
            else:
                # if no seats
                if guest_movement[i] not in waitlist:
                    waitlist.append(guest_movement[i])
                else:
                    # get bored and leave
                    waitlist.remove(guest_movement[i])

        elif eat[guest_movement[i]]==1:
            print(guest_movement[i])
            # if in seated, then remove it
            if guest_movement[i] in seated:
                seated.remove(guest_movement[i])
                seats_avail+=1
                # take guests from waitlist and make them seat
                # can give quadratic complexity in worst case
                while seats_avail>0 and len(waitlist)>0:
                    first_inline = waitlist.pop(0)
                    seated.add(first_inline)
                    eat[first_inline]=1
                    seats_avail-=1
            else:
                if seats_avail==0:
                    if guest_movement[i] not in waitlist:
                        waitlist.append(guest_movement[i])
                    else:
                        waitlist.remove(guest_movement[i])
                else:
                    seated.add(guest_movement[i])
                    seats_avail-=1
    return eat

if __name__=="__main__":
    res = main_fn(2,[10,15,5,8],[0,1,2,1,3,2,3,0])



