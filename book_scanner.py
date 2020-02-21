from sys import argv


def rank_libraries(libraries, books):
    return sorted(libraries, key=lambda library: library[2] / (library[3] * library[1]))

def search(filename):
    b = 0
    l = 0
    d = 0
    books = []
    libraries = []

    with open(filename + '.txt') as f:
        b, l, d = map(int, f.readline().split())

        for score in map(int, f.readline().split()):
            books.append([score, False])

        for j in range(l):
            nj, tj, mj = list(map(int, f.readline().split()))
            lib_books = list(map(int, f.readline().split()))
            lib_books.sort(key=lambda book: -books[book][0])
            libraries.append([j, nj, tj, mj, lib_books, [], False, False])

    libraries = rank_libraries(libraries, books)

    li = -1
    wait = 0
    used_library_count = 0

    for day in range(d):
        #print('Day', day + 1, 'of', d)
        
        if wait == 0:
            if li + 1 < l:
                li += 1
                wait = libraries[li][2]
                used_library_count += 1

        for x in range(li + 1):
            if libraries[x][7]:
                continue
            
            capacity = libraries[x][3]
            used = 0

            for book in libraries[x][4]:
                if not books[book][1]:
                    books[book][1] = True
                    used += 1
                    libraries[x][5].append(book)
                    
                    if used == capacity:
                        break

            if used == 0:
                libraries[x][7] = True
        
        wait = max(0, wait - 1)

    empty_count = 0

    for library in libraries[:used_library_count]:
        if len(library[5]) == 0:
            empty_count += 1

    used_library_count -= empty_count

    with open(filename + '.out', 'w') as g:
        g.write(str(used_library_count))
        g.write('\n')

        for x in range(l):
            library = libraries[x]

            if len(library[5]) == 0:
                continue
            
            g.write(str(library[0]) + ' ' + str(len(library[5])))
            g.write('\n')
            g.write(' '.join(str(bid) for bid in library[5]))            
            g.write('\n')

search("f_libraries_of_the_world")
