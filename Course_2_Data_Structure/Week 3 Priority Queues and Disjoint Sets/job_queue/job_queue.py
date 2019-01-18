# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def sift_down(self,i):
        ind_min = i
        l = 2 * i + 1
        if l < len(self.workers) and self.workers[l][1] < self.workers[ind_min][1]:
            ind_min = l
        elif (l < len(self.workers)) and (self.workers[l][1] == self.workers[ind_min][1]) and (self.workers[l][0] < self.workers[ind_min][0]):
            ind_min = l
        r = 2 * i + 2
        if r < len(self.workers) and (self.workers[r][1]< self.workers[ind_min][1]):
            ind_min = r
        elif (r < len(self.workers)) and (self.workers[r][1] == self.workers[ind_min][1]) and (self.workers[r][0] < self.workers[ind_min][0]):
            ind_min = r
        if ind_min != i:
            self.workers[i], self.workers[ind_min] = self.workers[ind_min], self.workers[i]
            
            self.sift_down(ind_min)


    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        self.workers = [(i,0) for i in range(self.num_workers)]
        for j in range(len(self.jobs)):
            self.assigned_workers[j] = self.workers[0][0]
            self.start_times[j] = self.workers[0][1]
            self.workers[0] = (self.workers[0][0],self.workers[0][1] + self.jobs[j])
            self.sift_down(0)
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

