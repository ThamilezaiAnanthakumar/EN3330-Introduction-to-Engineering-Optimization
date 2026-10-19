# %%
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.grid":True,"grid.alpha":0.35,"savefig.bbox":"tight"})

# %%
L=lambda mu,x: x**2+mu*(1-x)
d=lambda mu: mu-mu**2/4
cols=["C0","C1","C2","C3"]

# %%
# Q1(a)
x=np.linspace(-1.5,3,400)
fig,ax=plt.subplots(figsize=(6.5,4.2))
for mu,c in zip([0,1,2,3],cols):
    ax.plot(x,L(mu,x),c,label=rf"$\mu={mu}$")
    xm=mu/2; ax.plot(xm,L(mu,xm),"o",color=c,ms=7,mec="k")
    ax.annotate(rf"$x(\mu)={xm:g}$",(xm,L(mu,xm)),textcoords="offset points",xytext=(4,-16),fontsize=9,color=c)
ax.axvspan(-1.5,1,color="grey",alpha=0.12); ax.axvline(1,color="k",ls="--",lw=1)
ax.text(-1.4,7.3,"infeasible ($x<1$)",fontsize=9)
ax.set_ylim(-0.5,8); ax.set_xlabel("$x$"); ax.set_ylabel(r"$L(\mu,x)$")
ax.set_title(r"$L(\mu,x)=x^2+\mu(1-x)$"); ax.legend()
fig.savefig("fig/q1a.png")

# %%
# Q1(b)
m=np.linspace(0,4.5,300)
fig,ax=plt.subplots(figsize=(6.2,3.8))
ax.plot(m,d(m),"C0",lw=2,label=r"$d(\mu)=\mu-\mu^2/4$")
ax.axhline(1,color="C3",ls="--",lw=1,label=r"$p^*=1$")
ax.plot(2,1,"o",color="C3",ms=8,mec="k"); ax.annotate(r"$(\mu^*,d^*)=(2,1)$",(2,1),xytext=(2.4,0.55),arrowprops=dict(arrowstyle="->"))
for mu in [0,1,3]: ax.plot(mu,d(mu),"s",color="C0",ms=6)
ax.set_xlabel(r"$\mu$"); ax.set_ylabel(r"$d(\mu)$"); ax.set_title("Dual function"); ax.legend(loc="lower center")
fig.savefig("fig/q1b.png")

# %%
# Q1(c)
x=np.linspace(-1,3,500)
fig,ax=plt.subplots(figsize=(6.5,4.2))
for mu,c in zip([0,2,5,10,20],["C0","C1","C2","C4","C5"]):
    ax.plot(x,L(mu,x),c,lw=1,alpha=0.8,label=rf"$L({mu},x)$")
xf=x[x>=1]; ax.plot(xf,xf**2,"k",lw=3,label=r"$g(x)=x^2$ ($x\geq1$)")
ax.axvspan(-1,1,color="red",alpha=0.10)
ax.annotate("",xy=(0,12),xytext=(0,6),arrowprops=dict(arrowstyle="->",lw=2,color="red"))
ax.text(-0.85,10.5,r"$g(x)=+\infty$"+"\n(infeasible)",color="red")
ax.axvline(1,color="k",ls="--",lw=1); ax.plot(1,1,"o",color="C3",ms=8,mec="k")
ax.annotate(r"$\min g = g(1)=1$",(1,1),xytext=(1.4,-2.2),arrowprops=dict(arrowstyle="->"))
ax.set_ylim(-4,12); ax.set_xlabel("$x$"); ax.set_ylabel("value")
ax.set_title(r"Primal function $g(x)=\max_{\mu\geq0}L(\mu,x)$"); ax.legend(fontsize=8,loc="upper right")
fig.savefig("fig/q1c.png")

# %%
# Q2(a)(iv)
fig,(a1,a2)=plt.subplots(1,2,figsize=(9,3.4))
m=np.linspace(0,5,100); a1.plot(m,np.ones_like(m),"C0",lw=2)
a1.plot(2,1,"o",color="C3",ms=8,mec="k"); a1.annotate(r"$L(\mu^*,x^*)=1$",(2,1),xytext=(2.3,1.3),arrowprops=dict(arrowstyle="->"))
a1.set_ylim(0,2); a1.set_xlabel(r"$\mu$"); a1.set_title(r"$L(\mu,x^*)=L(\mu,1)=1$")
x=np.linspace(-1,3,200); a2.plot(x,(x-1)**2+1,"C1",lw=2)
a2.plot(1,1,"o",color="C3",ms=8,mec="k"); a2.annotate(r"$L(\mu^*,x^*)=1$",(1,1),xytext=(1.5,0.4),arrowprops=dict(arrowstyle="->"))
a2.set_ylim(0,5.5); a2.set_xlabel("$x$"); a2.set_title(r"$L(\mu^*,x)=(x-1)^2+1$")
fig.savefig("fig/q2a.png")

# %%
# Q3(b)
m=np.linspace(0,4,300)
fig,ax=plt.subplots(figsize=(6.5,4.2))
lines={0:m,1:np.ones_like(m),2:4-m}
for xx,c in zip([0,1,2],["C0","C1","C2"]):
    ax.plot(m,lines[xx],c,lw=1.3,label=rf"$x={xx}$: $L={['\\mu','1','4-\\mu'][xx]}$")
env=np.minimum.reduce([lines[0],lines[1],lines[2]])
ax.plot(m,env,"k",lw=3,label="lower envelope")
ax.plot(m,d(m),"r--",lw=2,label=r"true $d(\mu)=\mu-\mu^2/4$")
ax.set_ylim(-0.5,4); ax.set_xlabel(r"$\mu$"); ax.set_ylabel(r"$L(\mu,x)$")
ax.set_title(r"$L(\mu,x)$ as a function of $\mu$"); ax.legend(fontsize=9)
fig.savefig("fig/q3b.png")


