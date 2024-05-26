from collections import deque


def compute_day_gains(nb_seats, paying_guests, guest_movements):
    n = len(paying_guests)

    eated = [False for _ in range(n)]

    seated = set()  # Set of seated people at every step

    # Hash table {i: j indicating that person i entered the queue for the last

    # time at index j in guest_movements, if it is still there (otherwise i not in waiting)}

    waiting = {}

    # queue [(i, j)] indicating that person i entered at index j of guest_movements

    # the queue (possibly containing duplicates that will be ignored using waiting dictionary)

    queue = deque()

    # Main iteration

    for j in range(len(guest_movements)):

        # Get the person

        i = guest_movements[j]

        # Find whether the person is arriving or leaving

        if i in seated:  # The person is leaving the table

            # Remove that person from the table and process the next person that truly belons to the queue (is in waiting)

            seated.remove(i)

            # Start poping from the queue until an element from waiting is found or the queue becomes empty

            while queue:

                p, index = queue.popleft()

                if p in waiting and index == waiting[p]:  # This means that the person is the next in queue that can eat

                    # Sit the person

                    seated.add(p)

                    # Record that that person  p seated and ate

                    eated[p] = True

                    # Remove it from the waiting set

                    del waiting[p]

                    break



        elif i in waiting:  # The person got bored and left

            # Delete that person from waiting and ignore it if when poping from queue it is not on waiting

            del waiting[i]



        else:

            # The person is arriving

            # If the queue is empty, go directly and seat if possible

            if not queue and len(seated) < nb_seats:

                # Seat the person i

                seated.add(i)

                # Record that that person ate

                eated[i] = True

            else:

                # Add the person to the queue

                queue.append((i, j))

                # Record that the person just entered the queue at that index for the last time

                waiting[i] = j

    gain = sum(paying_guests[i] for i in range(n) if eated[i])

    return gain


# Sample Test Case
if __name__=="__main__":
    nb_seats = 2
    paying_guests = [10, 15, 5, 8]
    guest_movements = [0, 1, 2, 3, 2, 3, 2, 1, 2, 0]
    gain = compute_day_gains(nb_seats, paying_guests, guest_movements)











