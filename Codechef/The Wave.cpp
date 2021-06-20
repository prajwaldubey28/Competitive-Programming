# Q = https://www.codechef.com/COOK130B/problems/WAV2

#include<bits/stdc++.h>

using namespace std;

#define ll long long

#define FAST1 ios_base::sync_with_stdio(false);

#define FAST2 cin.tie(NULL);

#include<bits/stdc++.h>

using namespace std;

#define ll long long

#define FAST1 ios_base::sync_with_stdio(false);

#define FAST2 cin.tie(NULL);

void solve(){

 ll n,q;

cin>>n>>q;

 ll list1[n];

 for(ll i=0;i<n;i++)

 cin>>list1[i];

 sort(list1,list1+n);

for(ll i=0;i<q;i++){

 ll x;

 cin>>x;

ll x1=lower_bound(list1,list1+n,x)-list1;

 if(x1<n && list1[x1]==x)

cout<<0<<endl;

else if(x1%2==0)

cout<<"POSITIVE"<<endl;

else

cout<<"NEGATIVE"<<endl;
 }
}
int main(){

FAST1;

 FAST2;

 solve();



}