# Wrong invariants the bounded check accepts at k=10

Each one: the full verifier found a real violation, ESBMC found none within 10 unwindings.

## nested_delay_notd2_1.c::INVARIANT_MARKER_1  (easy, Qwen/Qwen3-0.6B)

Candidate invariant: `st == 0`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'REJECT'}. First bound that catches it: 50.

```c
int last;
int SIZE = 20;
int main()
{
  last = (int) rand();
  assume(last > 0);
  int a = 0;
  int b = 0;
  int c = 0;
  int st = 0;
  int d = 0;
  while (1)
  {
    INVARIANT_MARKER_1();
    st = 1;
    for (c = 0; c < SIZE; c++)
    {
      INVARIANT_MARKER_2();
      if (c >= last)
      {
        st = 0;
      }
    }

    if ((st == 0) && (c == (last + 1)))
    {
      a += 3;
      b += 3;
    }
    else
    {
      a += 2;
      b += 2;
    }
    if ((c == last) && (st == 0))
    {
      a = a + 1;
    }
    else
      if ((st == 1) && (last >= SIZE))
    {
      d++;
    }
    if (d == SIZE)
    {
      a = 0;
      b = 1;
    }
    assert((a == b) && (c == SIZE));
  }

  return 0;
}
```

## nested_delay_notd2_1.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `(c == 0 && a == 0 && b == 0) || (c == 1 && a == 1 && b == 1) || (c == 2 && a == 2 && b == 2) || (c == 3 && a == 3 && b == 3) || (c == 4 && a == 4 && b == 4) || (c == 5 && a == 5 && b == 5) || (c == 6 && a == 6 && b == 6) || (c == 7 && a == 7 && b == 7) || (c == 8 && a == 8 && b == 8) || (c == 9 && a == 9 && b == 9) || (c == 10 && a == 10 && b == 10) || (c == 11 && a == 11 && b == 11) || (c == 12 && a == 12 && b == 12) || (c == 13 && a == 13 && b == 13) || (c == 14 && a == 14 && b == 14) || (c == 15 && a == 15 && b == 15) || (c == 16 && a == 16 && b == 16) || (c == 17 && a == 17 && b == 17) || (c == 18 && a == 18 && b == 18) || (c == 19 && a == 19 && b == 19) || (c == 20 && a == 20 && b == 20)`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'REJECT'}. First bound that catches it: 50.

```c
int last;
int SIZE = 20;
int main()
{
  last = (int) rand();
  assume(last > 0);
  int a = 0;
  int b = 0;
  int c = 0;
  int st = 0;
  int d = 0;
  while (1)
  {
    INVARIANT_MARKER_1();
    st = 1;
    for (c = 0; c < SIZE; c++)
    {
      INVARIANT_MARKER_2();
      if (c >= last)
      {
        st = 0;
      }
    }

    if ((st == 0) && (c == (last + 1)))
    {
      a += 3;
      b += 3;
    }
    else
    {
      a += 2;
      b += 2;
    }
    if ((c == last) && (st == 0))
    {
      a = a + 1;
    }
    else
      if ((st == 1) && (last >= SIZE))
    {
      d++;
    }
    if (d == SIZE)
    {
      a = 0;
      b = 1;
    }
    assert((a == b) && (c == SIZE));
  }

  return 0;
}
```

## nested_delay_notd2_1.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `a % 2 == 0 && b % 2 == 0`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'REJECT'}. First bound that catches it: 50.

```c
int last;
int SIZE = 20;
int main()
{
  last = (int) rand();
  assume(last > 0);
  int a = 0;
  int b = 0;
  int c = 0;
  int st = 0;
  int d = 0;
  while (1)
  {
    INVARIANT_MARKER_1();
    st = 1;
    for (c = 0; c < SIZE; c++)
    {
      INVARIANT_MARKER_2();
      if (c >= last)
      {
        st = 0;
      }
    }

    if ((st == 0) && (c == (last + 1)))
    {
      a += 3;
      b += 3;
    }
    else
    {
      a += 2;
      b += 2;
    }
    if ((c == last) && (st == 0))
    {
      a = a + 1;
    }
    else
      if ((st == 1) && (last >= SIZE))
    {
      d++;
    }
    if (d == SIZE)
    {
      a = 0;
      b = 1;
    }
    assert((a == b) && (c == SIZE));
  }

  return 0;
}
```

## nested_delay_notd2_1.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 <= c && c < SIZE`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'REJECT'}. First bound that catches it: 50.

```c
int last;
int SIZE = 20;
int main()
{
  last = (int) rand();
  assume(last > 0);
  int a = 0;
  int b = 0;
  int c = 0;
  int st = 0;
  int d = 0;
  while (1)
  {
    INVARIANT_MARKER_1();
    st = 1;
    for (c = 0; c < SIZE; c++)
    {
      INVARIANT_MARKER_2();
      if (c >= last)
      {
        st = 0;
      }
    }

    if ((st == 0) && (c == (last + 1)))
    {
      a += 3;
      b += 3;
    }
    else
    {
      a += 2;
      b += 2;
    }
    if ((c == last) && (st == 0))
    {
      a = a + 1;
    }
    else
      if ((st == 1) && (last >= SIZE))
    {
      d++;
    }
    if (d == SIZE)
    {
      a = 0;
      b = 1;
    }
    assert((a == b) && (c == SIZE));
  }

  return 0;
}
```

## sll-01-1_8.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < end`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *inner;
} SLL;
int main()
{
  SLL *list = malloc(sizeof(SLL));
  list->next = NULL;
  ;
  SLL *end = list;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    end->next = malloc(sizeof(SLL));
    end = end->next;
    end->next = NULL;
    ;
  }

  end = NULL;
  end = list;
  while (NULL != end)
  {
    INVARIANT_MARKER_2();
    int len = 0;
    SLL *inner = end->inner;
    while (NULL != inner)
    {
      INVARIANT_MARKER_3();
      if (len == 0)
      {
        len = 1;
      }
      else
      {
        len = 2;
      }
      inner = inner->inner;
    }

    assert(len <= 1);
    end = end->next;
  }

  while (NULL != list)
  {
    INVARIANT_MARKER_4();
    end = list->inner;
    if (NULL != end)
    {
      free(end);
      end = NULL;
    }
    end = list->next;
    free(list);
    list = end;
  }

  return 0;
}
```

## sll-01-2_9.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < end`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *inner;
} SLL;
int main()
{
  SLL *list = malloc(sizeof(SLL));
  list->next = NULL;
  ;
  SLL *end = list;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    end->next = malloc(sizeof(SLL));
    end = end->next;
    end->next = NULL;
    ;
  }

  end = NULL;
  end = list;
  while (NULL != end)
  {
    INVARIANT_MARKER_2();
    int len = 0;
    SLL *inner = end->inner;
    while (NULL != inner)
    {
      INVARIANT_MARKER_3();
      if (len == 0)
      {
        len = 1;
      }
      else
      {
        len = 2;
      }
      inner = inner->inner;
      if (len == 1)
      {
        inner = inner->inner;
      }
    }

    end = end->next;
  }

  while (NULL != list)
  {
    INVARIANT_MARKER_4();
    end = list->inner;
    if (NULL != end)
    {
      assert(NULL != end);
      free(end);
      end = NULL;
    }
    end = list->next;
    free(list);
    list = end;
  }

  return 0;
}
```

## dll-queue-1_4.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < head`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *item = head;
  int status = 0;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item->next = malloc(sizeof(SLL));
    item->next->prev = item;
    item = item->next;
    item->next = NULL;
    if (!status)
    {
      item->data = 1;
      status = 1;
    }
    else
      if (status == 1)
    {
      item->data = 2;
      status = 2;
    }
    else
      if (status >= 2)
    {
      item->data = 3;
      status = 3;
    }
  }

  assert(head != NULL);
  if (status == 1)
  {
  }
  if (status == 2)
  {
  }
  if (status == 3)
  {
  }
  item = head->next;
  while (item && (int) rand())
  {
    INVARIANT_MARKER_2();
    item = item->next;
  }

  while (head)
  {
    INVARIANT_MARKER_3();
    item = head;
    head = head->next;
    free(item);
  }

  return 0;
}
```

## dll-queue-1_4.c::INVARIANT_MARKER_2  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < head`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *item = head;
  int status = 0;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item->next = malloc(sizeof(SLL));
    item->next->prev = item;
    item = item->next;
    item->next = NULL;
    if (!status)
    {
      item->data = 1;
      status = 1;
    }
    else
      if (status == 1)
    {
      item->data = 2;
      status = 2;
    }
    else
      if (status >= 2)
    {
      item->data = 3;
      status = 3;
    }
  }

  assert(head != NULL);
  if (status == 1)
  {
  }
  if (status == 2)
  {
  }
  if (status == 3)
  {
  }
  item = head->next;
  while (item && (int) rand())
  {
    INVARIANT_MARKER_2();
    item = item->next;
  }

  while (head)
  {
    INVARIANT_MARKER_3();
    item = head;
    head = head->next;
    free(item);
  }

  return 0;
}
```

## dll-queue-1_4.c::INVARIANT_MARKER_3  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < head`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *item = head;
  int status = 0;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item->next = malloc(sizeof(SLL));
    item->next->prev = item;
    item = item->next;
    item->next = NULL;
    if (!status)
    {
      item->data = 1;
      status = 1;
    }
    else
      if (status == 1)
    {
      item->data = 2;
      status = 2;
    }
    else
      if (status >= 2)
    {
      item->data = 3;
      status = 3;
    }
  }

  assert(head != NULL);
  if (status == 1)
  {
  }
  if (status == 2)
  {
  }
  if (status == 3)
  {
  }
  item = head->next;
  while (item && (int) rand())
  {
    INVARIANT_MARKER_2();
    item = item->next;
  }

  while (head)
  {
    INVARIANT_MARKER_3();
    item = head;
    head = head->next;
    free(item);
  }

  return 0;
}
```

## dll-rb-cnstr_1-2_4.c::INVARIANT_MARKER_3  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 <= list`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'TIMEOUT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef enum 
{
  RED,
  BLACK
} Colour;
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  Colour colour;
} SLL;
int main()
{
  SLL *list = malloc(sizeof(SLL));
  list->next = NULL;
  list->prev = NULL;
  list->colour = BLACK;
  SLL *end = list;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    end->next = malloc(sizeof(SLL));
    end->next->prev = end;
    end = end->next;
    end->next = NULL;
    if ((int) rand())
    {
      end->colour = BLACK;
    }
    else
    {
      end->colour = RED;
      end->next = malloc(sizeof(SLL));
      end->next->prev = end;
      end = end->next;
      end->next = NULL;
      end->colour = BLACK;
    }
  }

  end = NULL;
  end = list;
  while (NULL != end)
  {
    INVARIANT_MARKER_2();
    if (RED == end->colour)
    {
      end = end->next;
      end = end->next;
    }
    assert(end->next);
    end = end->next;
  }

  while (NULL != list)
  {
    INVARIANT_MARKER_3();
    if (RED == list->colour)
    {
      end = list->next;
      free(list);
      list = end->next;
      free(end);
    }
    else
    {
      end = list->next;
      free(list);
      list = end;
    }
  }

  return 0;
}
```

## dll-simple-white-blue-2_2.c::INVARIANT_MARKER_1  (hard, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < x`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *x = head;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    x->next = malloc(sizeof(SLL));
    x->next->prev = x;
    x = x->next;
    x->data = 0;
    x->next = NULL;
  }

  if ((int) rand())
  {
    x = malloc(sizeof(SLL));
    x->data = 1;
    x->next = head;
    x->prev = NULL;
    head = x;
  }
  else
  {
    x = head;
    while (x->next != NULL)
    {
      INVARIANT_MARKER_2();
      if ((int) rand())
      {
        break;
      }
      x = x->next;
    }

    SLL *y = x->next;
    x->next = malloc(sizeof(SLL));
    x->data = 1;
    x->next = y;
    if (y != NULL)
    {
      x->prev = y->prev;
      y->prev = x;
    }
  }
  x = head;
  while (x->data != 1)
  {
    INVARIANT_MARKER_3();
    x = x->next;
  }

  x = x->next;
  while (x)
  {
    INVARIANT_MARKER_4();
    if (x->data == 1)
    {
      assert(0);
    }
    x = x->next;
  }

  x = head;
  while (x != NULL)
  {
    INVARIANT_MARKER_5();
    head = x;
    x = x->next;
    free(head);
  }

  return 0;
}
```

## dll-simple-white-blue-2_2.c::INVARIANT_MARKER_1  (hard, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 <= x`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'ACCEPT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *x = head;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    x->next = malloc(sizeof(SLL));
    x->next->prev = x;
    x = x->next;
    x->data = 0;
    x->next = NULL;
  }

  if ((int) rand())
  {
    x = malloc(sizeof(SLL));
    x->data = 1;
    x->next = head;
    x->prev = NULL;
    head = x;
  }
  else
  {
    x = head;
    while (x->next != NULL)
    {
      INVARIANT_MARKER_2();
      if ((int) rand())
      {
        break;
      }
      x = x->next;
    }

    SLL *y = x->next;
    x->next = malloc(sizeof(SLL));
    x->data = 1;
    x->next = y;
    if (y != NULL)
    {
      x->prev = y->prev;
      y->prev = x;
    }
  }
  x = head;
  while (x->data != 1)
  {
    INVARIANT_MARKER_3();
    x = x->next;
  }

  x = x->next;
  while (x)
  {
    INVARIANT_MARKER_4();
    if (x->data == 1)
    {
      assert(0);
    }
    x = x->next;
  }

  x = head;
  while (x != NULL)
  {
    INVARIANT_MARKER_5();
    head = x;
    x = x->next;
    free(head);
  }

  return 0;
}
```

## dll-simple-white-blue-2_2.c::INVARIANT_MARKER_4  (hard, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < x || x == NULL`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *x = head;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    x->next = malloc(sizeof(SLL));
    x->next->prev = x;
    x = x->next;
    x->data = 0;
    x->next = NULL;
  }

  if ((int) rand())
  {
    x = malloc(sizeof(SLL));
    x->data = 1;
    x->next = head;
    x->prev = NULL;
    head = x;
  }
  else
  {
    x = head;
    while (x->next != NULL)
    {
      INVARIANT_MARKER_2();
      if ((int) rand())
      {
        break;
      }
      x = x->next;
    }

    SLL *y = x->next;
    x->next = malloc(sizeof(SLL));
    x->data = 1;
    x->next = y;
    if (y != NULL)
    {
      x->prev = y->prev;
      y->prev = x;
    }
  }
  x = head;
  while (x->data != 1)
  {
    INVARIANT_MARKER_3();
    x = x->next;
  }

  x = x->next;
  while (x)
  {
    INVARIANT_MARKER_4();
    if (x->data == 1)
    {
      assert(0);
    }
    x = x->next;
  }

  x = head;
  while (x != NULL)
  {
    INVARIANT_MARKER_5();
    head = x;
    x = x->next;
    free(head);
  }

  return 0;
}
```

## dll-simple-white-blue-2_2.c::INVARIANT_MARKER_4  (hard, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < x`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *x = head;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    x->next = malloc(sizeof(SLL));
    x->next->prev = x;
    x = x->next;
    x->data = 0;
    x->next = NULL;
  }

  if ((int) rand())
  {
    x = malloc(sizeof(SLL));
    x->data = 1;
    x->next = head;
    x->prev = NULL;
    head = x;
  }
  else
  {
    x = head;
    while (x->next != NULL)
    {
      INVARIANT_MARKER_2();
      if ((int) rand())
      {
        break;
      }
      x = x->next;
    }

    SLL *y = x->next;
    x->next = malloc(sizeof(SLL));
    x->data = 1;
    x->next = y;
    if (y != NULL)
    {
      x->prev = y->prev;
      y->prev = x;
    }
  }
  x = head;
  while (x->data != 1)
  {
    INVARIANT_MARKER_3();
    x = x->next;
  }

  x = x->next;
  while (x)
  {
    INVARIANT_MARKER_4();
    if (x->data == 1)
    {
      assert(0);
    }
    x = x->next;
  }

  x = head;
  while (x != NULL)
  {
    INVARIANT_MARKER_5();
    head = x;
    x = x->next;
    free(head);
  }

  return 0;
}
```

## dll-simple-white-blue-2_2.c::INVARIANT_MARKER_5  (hard, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < x || x == NULL`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  struct TSLL *prev;
  int data;
} SLL;
int main()
{
  SLL *head = malloc(sizeof(SLL));
  head->next = NULL;
  head->prev = NULL;
  head->data = 0;
  SLL *x = head;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    x->next = malloc(sizeof(SLL));
    x->next->prev = x;
    x = x->next;
    x->data = 0;
    x->next = NULL;
  }

  if ((int) rand())
  {
    x = malloc(sizeof(SLL));
    x->data = 1;
    x->next = head;
    x->prev = NULL;
    head = x;
  }
  else
  {
    x = head;
    while (x->next != NULL)
    {
      INVARIANT_MARKER_2();
      if ((int) rand())
      {
        break;
      }
      x = x->next;
    }

    SLL *y = x->next;
    x->next = malloc(sizeof(SLL));
    x->data = 1;
    x->next = y;
    if (y != NULL)
    {
      x->prev = y->prev;
      y->prev = x;
    }
  }
  x = head;
  while (x->data != 1)
  {
    INVARIANT_MARKER_3();
    x = x->next;
  }

  x = x->next;
  while (x)
  {
    INVARIANT_MARKER_4();
    if (x->data == 1)
    {
      assert(0);
    }
    x = x->next;
  }

  x = head;
  while (x != NULL)
  {
    INVARIANT_MARKER_5();
    head = x;
    x = x->next;
    free(head);
  }

  return 0;
}
```

## sll-buckets-2_3.c::INVARIANT_MARKER_1  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < bcki`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  int data;
} SLL;
typedef struct TBCK
{
  struct TBCK *next;
  SLL *list;
  int data;
} BCK;
int main()
{
  BCK *bucket = malloc(sizeof(BCK));
  bucket->data = 0;
  bucket->list = NULL;
  bucket->next = malloc(sizeof(BCK));
  BCK *bcki = bucket->next;
  bcki->data = 1;
  bcki->list = NULL;
  bcki->next = malloc(sizeof(BCK));
  bcki = bcki->next;
  bcki->data = 2;
  bcki->list = NULL;
  bcki->next = NULL;
  struct TSLL *item = NULL;
  struct TSLL *itr = NULL;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item = malloc(sizeof(SLL));
    item->next = NULL;
    if ((int) rand())
    {
      item->data = 0;
    }
    else
      if ((int) rand())
    {
      item->data = 1;
    }
    else
    {
      item->data = 2;
    }
    bcki = bucket;
    assert(item != NULL);
    while (bcki->data != item->data)
    {
      INVARIANT_MARKER_2();
      bcki = bcki->next;
    }

    if (bcki->list == NULL)
    {
      bcki->list = item;
    }
    else
    {
      itr = bcki->list;
      while (itr->next != NULL)
      {
        INVARIANT_MARKER_3();
        itr = itr->next;
      }

      itr->next = item;
    }
  }

  bcki = bucket;
  while (bcki != NULL)
  {
    INVARIANT_MARKER_4();
    item = bcki->list;
    bcki->list = NULL;
    while (item != NULL)
    {
      INVARIANT_MARKER_5();
      itr = item;
      item = item->next;
      free(itr);
    }

    bucket = bcki;
    bcki = bcki->next;
    free(bucket);
    bucket = NULL;
  }

  return 0;
}
```

## sll-buckets-2_3.c::INVARIANT_MARKER_2  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < bcki`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  int data;
} SLL;
typedef struct TBCK
{
  struct TBCK *next;
  SLL *list;
  int data;
} BCK;
int main()
{
  BCK *bucket = malloc(sizeof(BCK));
  bucket->data = 0;
  bucket->list = NULL;
  bucket->next = malloc(sizeof(BCK));
  BCK *bcki = bucket->next;
  bcki->data = 1;
  bcki->list = NULL;
  bcki->next = malloc(sizeof(BCK));
  bcki = bcki->next;
  bcki->data = 2;
  bcki->list = NULL;
  bcki->next = NULL;
  struct TSLL *item = NULL;
  struct TSLL *itr = NULL;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item = malloc(sizeof(SLL));
    item->next = NULL;
    if ((int) rand())
    {
      item->data = 0;
    }
    else
      if ((int) rand())
    {
      item->data = 1;
    }
    else
    {
      item->data = 2;
    }
    bcki = bucket;
    assert(item != NULL);
    while (bcki->data != item->data)
    {
      INVARIANT_MARKER_2();
      bcki = bcki->next;
    }

    if (bcki->list == NULL)
    {
      bcki->list = item;
    }
    else
    {
      itr = bcki->list;
      while (itr->next != NULL)
      {
        INVARIANT_MARKER_3();
        itr = itr->next;
      }

      itr->next = item;
    }
  }

  bcki = bucket;
  while (bcki != NULL)
  {
    INVARIANT_MARKER_4();
    item = bcki->list;
    bcki->list = NULL;
    while (item != NULL)
    {
      INVARIANT_MARKER_5();
      itr = item;
      item = item->next;
      free(itr);
    }

    bucket = bcki;
    bcki = bcki->next;
    free(bucket);
    bucket = NULL;
  }

  return 0;
}
```

## sll-buckets-2_3.c::INVARIANT_MARKER_2  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 <= bcki && 0 <= item`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  int data;
} SLL;
typedef struct TBCK
{
  struct TBCK *next;
  SLL *list;
  int data;
} BCK;
int main()
{
  BCK *bucket = malloc(sizeof(BCK));
  bucket->data = 0;
  bucket->list = NULL;
  bucket->next = malloc(sizeof(BCK));
  BCK *bcki = bucket->next;
  bcki->data = 1;
  bcki->list = NULL;
  bcki->next = malloc(sizeof(BCK));
  bcki = bcki->next;
  bcki->data = 2;
  bcki->list = NULL;
  bcki->next = NULL;
  struct TSLL *item = NULL;
  struct TSLL *itr = NULL;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item = malloc(sizeof(SLL));
    item->next = NULL;
    if ((int) rand())
    {
      item->data = 0;
    }
    else
      if ((int) rand())
    {
      item->data = 1;
    }
    else
    {
      item->data = 2;
    }
    bcki = bucket;
    assert(item != NULL);
    while (bcki->data != item->data)
    {
      INVARIANT_MARKER_2();
      bcki = bcki->next;
    }

    if (bcki->list == NULL)
    {
      bcki->list = item;
    }
    else
    {
      itr = bcki->list;
      while (itr->next != NULL)
      {
        INVARIANT_MARKER_3();
        itr = itr->next;
      }

      itr->next = item;
    }
  }

  bcki = bucket;
  while (bcki != NULL)
  {
    INVARIANT_MARKER_4();
    item = bcki->list;
    bcki->list = NULL;
    while (item != NULL)
    {
      INVARIANT_MARKER_5();
      itr = item;
      item = item->next;
      free(itr);
    }

    bucket = bcki;
    bcki = bcki->next;
    free(bucket);
    bucket = NULL;
  }

  return 0;
}
```

## sll-buckets-2_3.c::INVARIANT_MARKER_2  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 <= bcki`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  int data;
} SLL;
typedef struct TBCK
{
  struct TBCK *next;
  SLL *list;
  int data;
} BCK;
int main()
{
  BCK *bucket = malloc(sizeof(BCK));
  bucket->data = 0;
  bucket->list = NULL;
  bucket->next = malloc(sizeof(BCK));
  BCK *bcki = bucket->next;
  bcki->data = 1;
  bcki->list = NULL;
  bcki->next = malloc(sizeof(BCK));
  bcki = bcki->next;
  bcki->data = 2;
  bcki->list = NULL;
  bcki->next = NULL;
  struct TSLL *item = NULL;
  struct TSLL *itr = NULL;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item = malloc(sizeof(SLL));
    item->next = NULL;
    if ((int) rand())
    {
      item->data = 0;
    }
    else
      if ((int) rand())
    {
      item->data = 1;
    }
    else
    {
      item->data = 2;
    }
    bcki = bucket;
    assert(item != NULL);
    while (bcki->data != item->data)
    {
      INVARIANT_MARKER_2();
      bcki = bcki->next;
    }

    if (bcki->list == NULL)
    {
      bcki->list = item;
    }
    else
    {
      itr = bcki->list;
      while (itr->next != NULL)
      {
        INVARIANT_MARKER_3();
        itr = itr->next;
      }

      itr->next = item;
    }
  }

  bcki = bucket;
  while (bcki != NULL)
  {
    INVARIANT_MARKER_4();
    item = bcki->list;
    bcki->list = NULL;
    while (item != NULL)
    {
      INVARIANT_MARKER_5();
      itr = item;
      item = item->next;
      free(itr);
    }

    bucket = bcki;
    bcki = bcki->next;
    free(bucket);
    bucket = NULL;
  }

  return 0;
}
```

## sll-buckets-2_3.c::INVARIANT_MARKER_4  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 < bcki`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  int data;
} SLL;
typedef struct TBCK
{
  struct TBCK *next;
  SLL *list;
  int data;
} BCK;
int main()
{
  BCK *bucket = malloc(sizeof(BCK));
  bucket->data = 0;
  bucket->list = NULL;
  bucket->next = malloc(sizeof(BCK));
  BCK *bcki = bucket->next;
  bcki->data = 1;
  bcki->list = NULL;
  bcki->next = malloc(sizeof(BCK));
  bcki = bcki->next;
  bcki->data = 2;
  bcki->list = NULL;
  bcki->next = NULL;
  struct TSLL *item = NULL;
  struct TSLL *itr = NULL;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item = malloc(sizeof(SLL));
    item->next = NULL;
    if ((int) rand())
    {
      item->data = 0;
    }
    else
      if ((int) rand())
    {
      item->data = 1;
    }
    else
    {
      item->data = 2;
    }
    bcki = bucket;
    assert(item != NULL);
    while (bcki->data != item->data)
    {
      INVARIANT_MARKER_2();
      bcki = bcki->next;
    }

    if (bcki->list == NULL)
    {
      bcki->list = item;
    }
    else
    {
      itr = bcki->list;
      while (itr->next != NULL)
      {
        INVARIANT_MARKER_3();
        itr = itr->next;
      }

      itr->next = item;
    }
  }

  bcki = bucket;
  while (bcki != NULL)
  {
    INVARIANT_MARKER_4();
    item = bcki->list;
    bcki->list = NULL;
    while (item != NULL)
    {
      INVARIANT_MARKER_5();
      itr = item;
      item = item->next;
      free(itr);
    }

    bucket = bcki;
    bcki = bcki->next;
    free(bucket);
    bucket = NULL;
  }

  return 0;
}
```

## sll-buckets-2_3.c::INVARIANT_MARKER_5  (easy, idopinto/Wonda-Qwen3-4B-Instruct-2507-V2-gt2-e2)

Candidate invariant: `0 <= bcki`

Cheap verdicts by bound: {1: 'ACCEPT', 2: 'ACCEPT', 5: 'ACCEPT', 10: 'ACCEPT', 20: 'ACCEPT', 50: 'TIMEOUT'}. No bound up to 50 catches it.

```c
typedef struct TSLL
{
  struct TSLL *next;
  int data;
} SLL;
typedef struct TBCK
{
  struct TBCK *next;
  SLL *list;
  int data;
} BCK;
int main()
{
  BCK *bucket = malloc(sizeof(BCK));
  bucket->data = 0;
  bucket->list = NULL;
  bucket->next = malloc(sizeof(BCK));
  BCK *bcki = bucket->next;
  bcki->data = 1;
  bcki->list = NULL;
  bcki->next = malloc(sizeof(BCK));
  bcki = bcki->next;
  bcki->data = 2;
  bcki->list = NULL;
  bcki->next = NULL;
  struct TSLL *item = NULL;
  struct TSLL *itr = NULL;
  while ((int) rand())
  {
    INVARIANT_MARKER_1();
    item = malloc(sizeof(SLL));
    item->next = NULL;
    if ((int) rand())
    {
      item->data = 0;
    }
    else
      if ((int) rand())
    {
      item->data = 1;
    }
    else
    {
      item->data = 2;
    }
    bcki = bucket;
    assert(item != NULL);
    while (bcki->data != item->data)
    {
      INVARIANT_MARKER_2();
      bcki = bcki->next;
    }

    if (bcki->list == NULL)
    {
      bcki->list = item;
    }
    else
    {
      itr = bcki->list;
      while (itr->next != NULL)
      {
        INVARIANT_MARKER_3();
        itr = itr->next;
      }

      itr->next = item;
    }
  }

  bcki = bucket;
  while (bcki != NULL)
  {
    INVARIANT_MARKER_4();
    item = bcki->list;
    bcki->list = NULL;
    while (item != NULL)
    {
      INVARIANT_MARKER_5();
      itr = item;
      item = item->next;
      free(itr);
    }

    bucket = bcki;
    bcki = bcki->next;
    free(bucket);
    bucket = NULL;
  }

  return 0;
}
```

# Contradictions: UAutomizer proves it, ESBMC reports a violation

- benchmark46_disjunctive_1.c::INVARIANT_MARKER_1: `(x > 0) || (y > 0) || (z > 0)` (4 samples)
- benchmark24_conjunctive_1.c::INVARIANT_MARKER_1: `(k + 1) >= (n - i) || (i >= n)` (1 samples)
- prodbin-ll_unwindbound1_2.c::INVARIANT_MARKER_1: `a * b == x * y + z` (3 samples)
- prodbin-ll_unwindbound1_2.c::INVARIANT_MARKER_1: `x*y + z == a*b` (1 samples)
- prodbin-ll_unwindbound1_2.c::INVARIANT_MARKER_1: `z + x*y == a*b` (3 samples)
- prodbin-ll_unwindbound1_2.c::INVARIANT_MARKER_1: `z + x*y == a*b && y >= 0` (1 samples)
- benchmark24_conjunctive_1.c::INVARIANT_MARKER_1: `2*k + i >= n` (1 samples)
- prod4br-ll_unwindbound1_1.c::INVARIANT_MARKER_1: `q + a * b * p == x * y` (2 samples)
- prod4br-ll_unwindbound1_1.c::INVARIANT_MARKER_1: `(a * b) * p + q == x * y` (1 samples)
- prod4br-ll_unwindbound1_1.c::INVARIANT_MARKER_1: `x*y == a*b + q` (1 samples)
- prod4br-ll_unwindbound1_1.c::INVARIANT_MARKER_1: `(a * b + q) == x * y` (1 samples)
- prod4br-ll_unwindbound1_1.c::INVARIANT_MARKER_1: `x * y == a * b + q` (3 samples)
- geo3-ll_unwindbound2_1.c::INVARIANT_MARKER_1: `(x * (z - 1)) + a == az * y` (2 samples)
- cohendiv-ll_unwindbound100_1.c::INVARIANT_MARKER_2: `b == y * a && 2 * b == 2 * y * a` (1 samples)
- fermat1-ll_2.c::INVARIANT_MARKER_1: `4 * A + 4 * r == u * u - v * v - 2 * u + 2 * v` (3 samples)
- fermat1-ll_2.c::INVARIANT_MARKER_2: `(4 * A + 4 * r) == (u * u - v * v - 2 * u + 2 * v)` (1 samples)
- prod4br-ll_unwindbound5_1.c::INVARIANT_MARKER_1: `(a * b) * p + q == x * y` (1 samples)
- prod4br-ll_unwindbound5_1.c::INVARIANT_MARKER_1: `(a * b * p) + q == x * y` (1 samples)
- prodbin-ll_unwindbound2_3.c::INVARIANT_MARKER_1: `z + x*y == a*b && y >= 0` (2 samples)
- prodbin-ll_unwindbound2_3.c::INVARIANT_MARKER_1: `z + x*y == a*b && 1 <= b` (1 samples)
