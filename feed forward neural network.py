# ff_nn.py
import random, math

def sigmoid(x): return 1.0/(1.0+math.exp(-x))
def dsigmoid(y): return y*(1-y)

class NN:
    def __init__(self, n_in, n_hidden, n_out, lr=0.5):
        self.lr=lr
        self.w1=[[random.uniform(-1,1) for _ in range(n_in+1)] for __ in range(n_hidden)]
        self.w2=[[random.uniform(-1,1) for _ in range(n_hidden+1)] for __ in range(n_out)]
    def forward(self, x):
        x = x + [1]
        self.z = [sigmoid(sum(wi*xi for wi,xi in zip(w,x))) for w in self.w1]
        z_bias = self.z + [1]
        self.y = [sigmoid(sum(wi*zi for wi,zi in zip(w,z_bias))) for w in self.w2]
        return self.y
    def train(self, x, t):
        y=self.forward(x)
        # output deltas
        out_d = [(t_i - y_i)*dsigmoid(y_i) for t_i,y_i in zip(t,y)]
        # hidden deltas
        hidden_d=[]
        for j in range(len(self.z)):
            s = sum(self.w2[k][j]*out_d[k] for k in range(len(out_d)))
            hidden_d.append(s*dsigmoid(self.z[j]))
        # update w2
        z_bias = self.z + [1]
        for k in range(len(self.w2)):
            for j in range(len(self.w2[k])):
                self.w2[k][j] += self.lr * out_d[k] * z_bias[j]
        # update w1
        x_bias = x + [1]
        for j in range(len(self.w1)):
            for i in range(len(self.w1[j])):
                self.w1[j][i] += self.lr * hidden_d[j] * x_bias[i]

if __name__=="__main__":
    # XOR dataset
    nn=NN(2,3,1,lr=0.8)
    data=[([0,0],[0]),([0,1],[1]),([1,0],[1]),([1,1],[0])]
    for epoch in range(5000):
        x,t = random.choice(data)
        nn.train(x,t)
    for x,t in data:
        print(x, nn.forward(x), "expected", t)
