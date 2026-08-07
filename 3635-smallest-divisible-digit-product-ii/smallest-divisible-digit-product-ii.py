class Solution(object):
    def smallestNumber(self, num, t):
        e2=e3=e5=e7=0
        while t%2==0:
            e2+=1; t//=2
        while t%3==0:
            e3+=1; t//=3
        while t%5==0:
            e5+=1; t//=5
        while t%7==0:
            e7+=1; t//=7
        if t!=1:
            return "-1"
        E2,E3,E5,E7 = e2,e3,e5,e7
        cd = {1:(0,0,0,0),2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),
              5:(0,0,1,0),6:(1,1,0,0),7:(0,0,0,1),8:(3,0,0,0),9:(0,2,0,0)}
        sz2,sz3,sz5,sz7 = E2+1,E3+1,E5+1,E7+1
        stride2 = sz3*sz5*sz7
        stride3 = sz5*sz7
        stride5 = sz7
        P = (E2+1)*stride2
        INF = 10**9
        f = [INF]*P
        def idx(n2,n3,n5,n7):
            return n2*stride2 + n3*stride3 + n5*stride5 + n7
        f[ idx(0,0,0,0) ] = 0
        for n2 in range(sz2):
            for n3 in range(sz3):
                for n5 in range(sz5):
                    for n7 in range(sz7):
                        i = n2*stride2 + n3*stride3 + n5*stride5 + n7
                        if i==0: continue
                        best = INF
                        for c2,c3,c5,c7 in cd.values():
                            p2 = n2-c2
                            if p2<0: p2=0
                            p3 = n3-c3
                            if p3<0: p3=0
                            p5 = n5-c5
                            if p5<0: p5=0
                            p7 = n7-c7
                            if p7<0: p7=0
                            prev = f[p2*stride2 + p3*stride3 + p5*stride5 + p7]
                            if prev+1 < best:
                                best = prev+1
                        f[i] = best
        full_idx = idx(E2,E3,E5,E7)
        if f[full_idx]>=INF:
            return "-1"
        N = len(num)
        digits = list(map(int,num))
        def feasible(rem,n2,n3,n5,n7):
            if n2<0: n2=0
            elif n2> E2: n2=E2
            if n3<0: n3=0
            elif n3> E3: n3=E3
            if n5<0: n5=0
            elif n5> E5: n5=E5
            if n7<0: n7=0
            elif n7> E7: n7=E7
            return rem >= f[n2*stride2 + n3*stride3 + n5*stride5 + n7]
        def suffix_fill(n2,n3,n5,n7,rem):
            res=[]
            for k in range(rem):
                rem_left = rem-k-1
                for d in range(1,10):
                    c2,c3,c5,c7 = cd[d]
                    nn2 = n2-c2
                    if nn2<0: nn2=0
                    if nn2> E2: nn2=E2
                    nn3 = n3-c3
                    if nn3<0: nn3=0
                    if nn3> E3: nn3=E3
                    nn5 = n5-c5
                    if nn5<0: nn5=0
                    if nn5> E5: nn5=E5
                    nn7 = n7-c7
                    if nn7<0: nn7=0
                    if nn7> E7: nn7=E7
                    if rem_left >= f[nn2*stride2 + nn3*stride3 + nn5*stride5 + nn7]:
                        res.append(d)
                        n2,n3,n5,n7 = nn2,nn3,nn5,nn7
                        break
                else:
                    return None
            return res
        prefix=[]
        stack=[]
        need2,need3,need5,need7 = E2,E3,E5,E7
        pos=0
        while pos < N:
            d0 = digits[pos]
            if d0>0:
                c2,c3,c5,c7 = cd[d0]
                nn2 = need2-c2
                nn3 = need3-c3
                nn5 = need5-c5
                nn7 = need7-c7
                if nn2<0: nn2=0
                if nn3<0: nn3=0
                if nn5<0: nn5=0
                if nn7<0: nn7=0
                rem = N-pos-1
                if feasible(rem, nn2,nn3,nn5,nn7):
                    stack.append((pos,need2,need3,need5,need7))
                    prefix.append(d0)
                    need2,need3,need5,need7 = nn2,nn3,nn5,nn7
                    pos+=1
                    continue
            if pos==N:
                return "".join(map(str,prefix))
            bump_list=[(pos,need2,need3,need5,need7,d0)]
            for (pj,p2,p3,p5,p7) in reversed(stack):
                bump_list.append((pj,p2,p3,p5,p7,digits[pj]))
            for (j,b2,b3,b5,b7,bd) in bump_list:
                rem = N-j-1
                for cand in range(bd+1,10):
                    if cand==0: continue
                    c2,c3,c5,c7 = cd[cand]
                    nn2 = b2-c2
                    nn3 = b3-c3
                    nn5 = b5-c5
                    nn7 = b7-c7
                    if nn2<0: nn2=0
                    if nn3<0: nn3=0
                    if nn5<0: nn5=0
                    if nn7<0: nn7=0
                    if feasible(rem, nn2,nn3,nn5,nn7):
                        res = prefix[:j] + [cand]
                        suf = suffix_fill(nn2,nn3,nn5,nn7,rem)
                        if suf is None: continue
                        return "".join(map(str,res+suf))
            break
        if pos==N:
            return "".join(map(str,prefix))
        min_len = f[full_idx]
        L2 = max(N+1, min_len)
        suf2 = suffix_fill(E2,E3,E5,E7, L2)
        if suf2 is None:
            return "-1"
        return "".join(map(str,suf2))