BiocManager::install("RColorBrewer")
library(RColorBrewer)
c=vector()
for (i in 1:nrow(surivalstatus)){
  count=0
  for (j in surivalstatus[i,2:ncol(surivalstatus)]){
    count=count+1
    if(j == 0){
      c[i]=count
      break
    }
  }
}
##}
print(c)
c[is.na(c)]= ncol(surivalstatus)-1
status=c(rep(1,times=length(c)))
group=surivalstatus$`Days after inoculation`
group=factor(group)
install.packages("BiocManager")
BiocManager::install("survival")
library(survival)
fit = survfit(Surv(c,status)~group)
plot( fit, ylab="Survival", xlab="Days",col=brewer.pal(n = 5,name="RdBu") ,mark.time = T,lwd = 5)
legend("bottomleft", col=brewer.pal(n = 5,name="RdBu") ,legend=levels(group),lwd = 5)



