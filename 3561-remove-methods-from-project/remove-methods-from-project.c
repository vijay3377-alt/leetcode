#include <stdlib.h>
void dfs(int node, int** graph, int* graphSize, int* visited)
{
    if (visited[node])
        return;
    visited[node] = 1;
    for (int i = 0; i < graphSize[node]; i++)
    {
        dfs(graph[node][i], graph, graphSize, visited);
    }
}
int* remainingMethods(int n, int k, int** invocations, int invocationsSize,
                      int* invocationsColSize, int* returnSize)
{
    int** graph = (int**)malloc(n * sizeof(int*));
    int* graphSize = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < invocationsSize; i++)
    {
        graphSize[invocations[i][0]]++;
    }
    for (int i = 0; i < n; i++)
    {
        graph[i] = (int*)malloc(graphSize[i] * sizeof(int));
        graphSize[i] = 0;
    }
    for(int i=0;i<invocationsSize;i++)
    {
        int a=invocations[i][0];
        int b=invocations[i][1];
        graph[a][graphSize[a]++]=b;
    }
    int* visited=(int*)calloc(n, sizeof(int));
    dfs(k,graph,graphSize,visited);
    for(int i=0;i<invocationsSize;i++)
    {
        int a=invocations[i][0];
        int b=invocations[i][1];
        if(!visited[a] && visited[b])
        {
            int* ans=(int*)malloc(n*sizeof(int));
            for(int j=0;j<n;j++)
                ans[j]=j;
            *returnSize=n;
            for(int j=0;j<n;j++)
                free(graph[j]);
            free(graph);
            free(graphSize);
            free(visited);
            return ans;
        }
    }
    int count=0;
    for(int i=0;i<n;i++)
    {
        if(!visited[i])
            count++;
    }
    int* ans=(int*)malloc(count*sizeof(int));
    int idx = 0;
    for(int i=0;i<n;i++)
    {
        if(!visited[i])
            ans[idx++] = i;
    }
    *returnSize=count;
    for(int i=0;i<n;i++)
        free(graph[i]);
    free(graph);
    free(graphSize);
    free(visited);
    return ans;
}