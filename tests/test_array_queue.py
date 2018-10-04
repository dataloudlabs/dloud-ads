from dloud_ads import array_queue

def test_dummy():
	Q = array_queue.ArrayQueue()
	
	assert Q.is_empty() == True
	assert len(Q) == 0

	Q.enqueue(2)
	assert Q.is_empty() == False
	assert len(Q) == 1
	assert Q.dequeue() == 2

	_ = [Q.enqueue(x) for x in range(4)]
	assert len(Q) == 4
	assert [Q.dequeue() for x in range(4)] == [0,1,2,3]
	assert len(Q) == 0

	_ = [Q.enqueue(x) for x in range(9)]
	assert len(Q) == 9
	assert len(Q._data) == 10

	_ = [Q.enqueue(x) for x in range(2)]
	assert len(Q) == 11
	assert len(Q._data) == 20

	assert [Q.dequeue() for x in range(11)] == [0,1,2,3,4,5,6,7,8,0,1]

