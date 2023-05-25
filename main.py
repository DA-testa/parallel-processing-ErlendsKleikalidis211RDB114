def parallel_processing(n, m, data):
  output = []
  threads = [(i, 0) for i in range(n)]

  for i in range(m):
    thread = min(threads, key=lambda x: x[1])
    output.append((thread[0], thread[1]))
    threads.remove(thread)
    threads.append((thread[0], thread[1] + data[i]))

  return output


def main():
  n, m = map(int, input().split())
  data = list(map(int, input().split()))

  result = parallel_processing(n, m, data)
  
  for thread, start_time in result:
    print(thread, start_time)


if __name__ == "__main__":
  main()
