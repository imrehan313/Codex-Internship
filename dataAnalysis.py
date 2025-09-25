import pandas as pd,matplotlib.pyplot as plt,seaborn as sb,os,random as r

(fileName := input("Enter the file name for csv data: ").strip()+".csv")

def main():
    try:
        if not os.path.exists(fileName):
         print(f"There is no such file available in {os.path.abspath(os.getcwd())} directory")

        df= pd.read_csv(fileName)  
        print(df.head(len(df)),"\n\n\n",round(df.describe(),2)) 
        # df = df.apply(pd.to_numeric)
        
        colDict={}
        for i,j in enumerate(df,start=1):
         colDict.update({i:j})
        print(f"\n\n\nThe Dictionary of Columns :\n {colDict}\n\n\n")

        numCols=df.select_dtypes(include=['number']).columns.tolist()

        for x,y in enumerate(numCols):
         numCols.pop(x) if "id" in y.lower() else ""

        print(f"Only These columns can be used for visualization :\n {numCols}\n\n")
        print(f"Average Score from:\n {(avg_scores := df[numCols].mean())}\n\n")
       
        avgCol=int(input("Select the column for average calculation: "))
        print(df[colDict.get(avgCol)].mean(),"\n\n")

        Colors=[]
        def barView():
            choice="0123456789abcdef"  
            for _ in range(len(numCols)):
                color = "#" +"".join(r.choices(choice, k=6))
                Colors.append(color)
        
            plt.figure(figsize=(8,4))
            avg_scores.plot(kind='bar',color=Colors)
            plt.title(f"Average Score from {fileName} using bar charts", fontsize=16)
            plt.ylabel("Average Score")
            plt.xticks(rotation=0)
            plt.grid(axis='y', linestyle='--', alpha=0.8)
            plt.show(block=False)
        
        def scatterView():
            plt.figure(figsize=(8,4))
            sb.scatterplot(data=df[numCols].mean(), s=350, color=Colors)
            plt.title(f"Average Score from {fileName} using Scatter Plots", fontsize=16)
            plt.ylabel('Average Score')
            plt.grid(True, linestyle='--', alpha=0.8)
            plt.show(block=False)

        def heatmapView():
            plt.figure(figsize=(8,4))
            correlation_matrix = df[numCols].corr()
            sb.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt='.2f')
            plt.title('Correlation Heatmap', fontsize=16)
            plt.show(block=False)

        def run():
         
         if "yes" in (q:=input(f"Do you want to visualize average scores of each column from {fileName} (y/n) : ").lower()) or "y" in q.lower():   
            barView()
            scatterView()
            heatmapView()
            plt.show()
         elif "n" in q.lower() or "no" in q.lower():
            print("Thank You")
         else:
            print("Invalid Input")
            
        run()

    except Exception as e:
        print(e)

if __name__=="__main__":
    main()
    