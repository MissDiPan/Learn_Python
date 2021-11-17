from __future__ import print_function
import torch


def create_t():
    x = torch.empty(5, 3)
    print(x)
    x = torch.zeros(5, 3, dtype=torch.long)
    print(x)
    x = torch.tensor([5.5, 3])
    print(x)

    x = x.new_ones(5, 3, dtype=torch.double)
    print(x)

    x = torch.randn_like(x, dtype=torch.float)  # same size, override
    print(x)
    print(x.size())


def process_t():
    x = torch.ones(3, 2) * 3
    y = torch.ones(3, 2) * 1
    print(x + y)
    print(torch.add(x, y))

    result = torch.empty(3, 2)
    torch.add(x, y, out=result)
    print(result)

    y.add_(x)  # add x to y
    print(y)

    print(x[:, 1])

    x = torch.randn(4, 4)
    y = x.view(16)  # 1*16 reshape
    z = x.view(-1, 8)  # (16/8)*8, -1 decided by another dimension
    print(x.size(), y.size(), z.size())


def autograd_t():
    a = torch.randn(2, 2)
    a = (a * 3) / (a - 1)
    print(a.requires_grad)
    a.requires_grad_(True)
    print(a.requires_grad)
    b = (a * a).sum()
    print(b.grad_fn)

    x = torch.ones(2, 2, requires_grad=True)  # default false
    print(x)
    y = x + 2
    print(y)
    print(y.grad_fn)

    z = y * y * 3
    out = z.mean()
    print(z, out)

    out.backward()
    print(x.grad)

    x = torch.randn(3, requires_grad=True)
    y = x * 2
    while y.data.norm() < 1000:
        y = y * 2
    print(y)

    print(x.requires_grad)
    print((x ** 2).requires_grad)

    with torch.no_grad():
        print((x ** 2).requires_grad)


def vectorization_t():
    w = torch.tensor([1, 2, 3])
    x = torch.tensor([1, 2, 3])
    print(torch.dot(w, x))


vectorization_t()
