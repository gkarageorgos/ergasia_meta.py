def the_set_of_movements(word, top):
    for i in range(len(word)):
        if word[i] == "3":
            if top == "$":
                top = "|"
            stack.append(top)
            print("At %d action: stack:%s entrance:%s situation:A" % (i + 2, stack, word[i + 1:]))
        elif word[i] == "6":
            if top == "$":
                print('When the  symbol at the top of the stack is $,'
                      ' the current entrance symbol is "6" and '
                      'the current situation is A the movement cannot be defined')
                print("No")
                return -1
            elif top == "|":
                stack.pop()
                top = stack[-1]
                print("At %d action: stack:%s entrance:%s situation:A" % (i + 2, stack, word[i + 1:]))
    if top == "$":
        print("YES")
    elif top == "|":
        print("NO")


print('K={A}\nΣ={"3", "6"}\nΓ={$, |}\nδ=δ{(Α,|,"3")=(PUSH(|)),δ(Α,|,"6")=(POP),\nδ(Α,$,"3")=(PUSH(|))}\nq0=A\nz0=$')
stack = []
W = input("Give a string to be read:")
stack.append("$")
print("At 1 action: stack:%s entrance:%s situation:A" % (stack, W))
the_set_of_movements(W, "$")
