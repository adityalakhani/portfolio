---
title: Can't Beat OAuth2
desc: Let's learn open authentication (OAuth) in 2 mins.
date_posted: December 21, 2024
tags: [security, web]
slug: cant-beat-oauth2
---

OAuth2 is an **authorization framework** that allows third-party applications to access user resources **without exposing user credentials**.

>  Think of it as a valet key for your data — limited access without giving away the whole keyring.

---

##  How It Works

1. **User** logs in via the **Authorization Server**.
2. Server returns an **Authorization Code** to the **Client App**.
3. Client app exchanges this code for an **Access Token**.
4. Client uses the access token to fetch data from the **Resource Server**.

---

##  Key Components

| Component           | Description                                 |
|---------------------|---------------------------------------------|
| `Authorization Server` | Authenticates user and issues tokens       |
| `Resource Server`       | Hosts user data (like profile, calendar) |
| `Client`                | The app requesting access                 |
| `Access Token`          | A short-lived token to access resources  |

---

##  Why Use OAuth2?

-  **Secure** – Never shares user passwords
-  **Scalable** – Widely adopted across platforms
-  **User-Friendly** – Familiar flows (e.g., "Login with Google")

---

##  Example: OAuth2 Flow in Python

```python
import requests

# Step 1: Redirect user to authorization server
auth_url = (
    "https://auth-server.com/authorize?"
    "client_id=your_client_id&"
    "redirect_uri=your_redirect_uri&"
    "response_type=code"
)
print("Visit this URL to authorize:", auth_url)

# Step 2: Exchange authorization code for access token
code = "user_auth_code"  # You'd get this from the redirect URI
token_url = "https://auth-server.com/token"

response = requests.post(token_url, data={
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "code": code,
    "grant_type": "authorization_code",
    "redirect_uri": "your_redirect_uri"
})

access_token = response.json().get("access_token")
print("Access Token:", access_token)
```

>  **Note:** Never expose your `client_secret` in frontend code or public repos.

---

##  Learn More

Check out the official docs at [OAuth.net](https://oauth.net/2/)

---

🛡️ OAuth2 makes modern apps secure and user-centric. Mastering it is a must for anyone building on the web today.
import Image from "next/image"
import BlogHeader from '../app/components/BlogHeader'

<BlogHeader date='2024-12-21'>
  <h1 className="m-0 p-0">Can't beat OAuth2.</h1>
  ## Let's learn **open authorization(OAuth)** in 2 mins. No prior knowledge needed
  <p className="tag">Tech</p>
  <p className="tag">2 min read</p>
  <p className="tag">Teaching</p>
</BlogHeader>

<blockquote className="border-l-4 border-info pl-4 italic my-6 mt-10 mb-0">
  Before starting let's keep these things in mind about OAuth:
  <ul className="list-disc">
    <li>Stands for Open Authorization (GO FOSS!)</li>
    <li>This a high level introduction, future part will cover implementation and in-depth information</li>
    <li>Used for Authorization and not authentication (there is a catch tho!)</li>
    <li>It is not our **lord and savior** but it solves a lot of things for us</li>
    <li>It does have security concerns</li>
  </ul>
</blockquote>

<div className="mt-10 mb-4">
<h1 className="m-0 p-0">Why do we need it?</h1>
</div>

Keeping it very short! To best understand the need of such a protocol we should look at how it helps us in our daily internet lives.

Imagine visiting a website that requires credentials before you can access its wonderful services (I see you, Chegg!). You go to their login page only to find that it asks for your email address and password. If you're like me, you'd be pissed by this absurdity. But then you spot those oddly shaped buttons at the bottom. Upon closer inspection, you realize they feature familiar faces, and you actually have accounts with some of them. After a few clicks, voila! you’re in the website and can go about your day.
All this couldn't have had happened without our darling OAuth protocol 🥂.

<div className="mt-6 mb-2">
<h2 className="m-0 p-0">Authorization is not authentication</h2>
</div>
At this point, you might have got some idea about OAuth. I would like to make it clear that OAuth is not an authentication technique it is an <span className="underline">**authorization**</span> technique. You might need to authenticate yourself to grant the necessary permissions but OAuth as a protocol does not care about authentication.
To understand the difference between **<ins>authentication</ins>** and <ins>**authorization**</ins>, consider what questions they ask individually.

<ul className="list-disc">
  <li> <ins>Authentication</ins> - **Who is it ?**</li>
  <li> <ins>Authorization</ins> - **What can they access?**</li>
  <li> <ins>Together they question</ins> - **Who is it and what can they access?**</li>
</ul>

So, Oauth just questions the **"What"** part of our security equation. **"Who"** part is a by-product and doesn't gurantee security by any means.
<blockquote className="border-l-4 border-quote pl-4 italic my-6 mt-4 mb-0">
  "Why do I need so many paasswordss! Can't it be simpler. Anyways my password is ..."
  <footer className="text-sm mt-2">— Miss Joe on a scam call</footer>
</blockquote>

<div className="mt-10 mb-4">
<h1 className="m-0 p-0">How does it work?</h1>
</div>
To explain in simple terms, we will take an example of the classic cryptography duo, Alice and Bob. Let's say Alice wants to view Bob's progress in the gym and decides to ask the gym for this information. It is important that the gym knows whether Alice is allowed to view the progress data. To tackle this, Bob can ask the gym to assign Alice a token that will serve as a testament to the fact that Bob has allowed Alice to view specific data on his behalf.
For all my visual learners, **Take a look at the image below**.

<div className="relative w-full lg:max-w-[50rem] mx-auto mt-[10px] mb-[10px]
 sm:max-w-[30rem] md:max-w-[50rem] p-4 border-[1.5px] border-imgborder rounded-[3px]"
 >
    <Image
      src="/nontech-oauth.png"
      alt="non-tech oauth information"
      width={300}
      height={333}
      className="rounded object-cover w-full"
      priority
    />
</div>

I hope the image does help you with your understanding of this protocol. I would also like to share a more techy diagram for this concept which we will discuss and explain in the next part.

<div className="relative w-full lg:max-w-[50rem] mx-auto mt-[10px] mb-[10px]
 sm:max-w-[30rem] md:max-w-[50rem] p-4 border-[1.5px] border-imgborder rounded-[3px]"
 >
    <Image
      src="/techintro-oauth.png"
      alt="non-tech oauth information"
      width={300}
      height={333}
      className="rounded object-cover w-full"
      priority
    />
</div>

<blockquote className="border-l-4 border-info pl-4 italic my-6 mt-2 mb-0">
  **NOTE :** OAuth protocol is infamous for being complex and confusing, while that discussion does have some weight, our focus on this technology for this part of blog, mainly revolves around its abstractions. 
</blockquote>

<div className="mt-10 mb-2">
<h1 className="m-0 p-0">Next part....</h1>
</div>

I would love to go over the code implementation of OAuth in <ins>**2 mins**</ins>. We will see what our sample **<ins>request</ins>** and **<ins>response</ins>** contains. My choice would be a javascript based auth library, <a className="underline text-hyperlink" href="https://www.authjs.dev">authjs.dev</a> . It makes OAuth insanely simple and intuitive.
I will update the link to second part here, untill then **See ya!**