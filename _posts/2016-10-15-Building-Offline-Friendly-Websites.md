---
title: Building Offline-Friendly Websites
---

##Downloading (almost) any website for offline access
·         For most content-focused websites, you can download a local copy of them to view offline. Once saved locally, you can copy them to a USB stick, CD, or shared drive, and open them offline with an ordinary browser.

·         To download a website locally, you can run this simple command from any OSX/Linux box. If you prefer a GUI, you can also use HTTrack (Windows & Linux) or SiteSucker (OSX). Command line examples below – this will download most websites within a few minutes. Subfolders are OK. Parameters are case sensitive.
o   Syntax: wget –mkEpnp http://website.com/
o   Examples:
§  wget –mkEpnp http://kompak.or.id/
§  wget –mkEpnp http://digitakarya.com/kompak/

·         For developers
o   This approach useful if you want to design in a CMS like WordPress and then render as a backend-less ‘static site’ (what Hari is doing now).
o   If you’re interested in developing static websites from scratch without a CMS, check out Jekyll – a popular static site generator that supports the Liquid templating engine (includes, variables, if/else, for loops, etc). Can also parse CSV & JSON files – useful for rapid prototyping.
o   If the sites are already mobile-friendly (eg responsive/Bootstrap), you can also easily turn them into Android/iOS apps that work offline with Phonegap or Cordova.
o   If you’re really interested, read this blog post: How We Build CMS-Free Websites
 
 
Making forms work offline
·         Saving a website for offline access works great for static content, but since there’s no server for the frontend to talk to, any form that sends a HTTP POST request (like a search box) will likely fail. By default, any inputs wrapped in <form></form> fields will send a POST request when the Submit button is clicked, so those won’t work.
 
·         If you want to create an interactive offline experience that uses forms, use Javascript with onclick() or other event listeners instead of doing traditional HTTP POST requests. This application logic should reside on the client side (usually in a .js file).
o   jQuery makes this REALLY EASY to do.
o   For advanced JavaScript developers, you can use an MVC framework like Backbone or Angular which handle data models & page routing very well – but there’s a bit of a learning curve, so learn at your own risk! I can’t claim much experience with these.

·         For website that collects a lot of data, like a survey or the Sekola Desa game, check out survey.js. It’s free & open source, including the drag & drop survey builder. You can save the entire survey definition as a single JSON file, and still add your own custom HTML/CSS/JS wherever. Could save a lot of time in developing survey-like apps that work offline.

·         To have an offline app send data to a server when it’s online, we need to use AJAX to push data to a server. You can do this with jQuery using $.post(), if you have a server that’s listening and ready to receive the data.
o   You should build your client-side logic so that even if the post() request fails, the app still continues to work using the local memory (session, cookie, LocalStorage, whatever).
o   But, it’s a lot of work to set and maintain up your own server, and then you have to build a whole server-side application with a API that’s always listening for your client app to transmit data. And as your data model/forms evolve on the client app, you’ll have to keep updating it on the server. And you’ll have to build interfaces for non-developers to get data out of the server. So a much faster way is to use something like Google’s Firebase.

·         Firebase offers a JavaScript library which you can add to any web app, online or offline. It lets your JavaScript easily communicate with the hosted Realtime Database, which is free for 100 simultaneous connections and 1GB of stored data. Since simultaneous means the same second, and data stored is only text, this should be more than enough for tens of thousands of users every week (and what we do at KOMPAK), and it’s very cheap to scale from there.
o   Firebase is great for offline apps because it first saves everything to the local offline database, and then synchronizes with the hosted database when there is a connection.
o   It can also tell the browser when the internet connects or disconnects, so you can make things happen automatically or ask the user to do something when that happens (see enabling offline capabilities).