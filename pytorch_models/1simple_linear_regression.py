import numpy as np
import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt

x_values = [i for i in range(11)]
x_train = np.array(x_values, dtype=np.float32)
x_train = x_train.reshape(-1, 1)

y_values = [2 * i + 1 for i in x_values]
y_train = np.array(y_values, dtype=np.float32)
y_train = y_train.reshape(-1, 1)


class LinearRegression(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    def forward(self, x):
        out = self.linear(x)
        return out


input_dim = 1
output_dim = 1
learning_rate = 0.01
epochs = 100
model = LinearRegression(input_dim, output_dim)

if torch.cuda.is_available():
    model.cuda()


criteria = torch.nn.MSELoss()
optimizer = torch.optimizer.SGD(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
    if torch.cuda.is_available():
        inputs = Variable(torch.from_numpy(x_train).cuda())
        labels = Variable(torch.from_numpy(y_train).cuda())
    else:
        inputs = Variable(torch.from_numpy(x_train))
        labels = Variable(torch.from_numpy(y_train))

    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criteria(outputs, labels)
    print(loss)
    loss.backward()
    optimizer.step()
    print(f"epoch {epoch}, loss {loss.item}")

with torch.no_grad():
    if torch.cuda.is_available():
        predicted = model(Variable(torch.from_numpy(x_train).cuda())).cpu().data.numpy()
    else:
        predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()
    print(predicted)

plt.clf()
plt.plot(x_train, y_train, "go", label="True data", alpha=0.5)
plt.plot(x_train, predicted, "--", label="Predictions", alpha=0.5)
plt.legend(loc="best")
plt.show()
