---
layout: post
title:  "Coders’ forbidden vocabula"
date:   2014-03-24 15:34:26 +0000
categories: ['Programming']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=846
---


Coders’ forbidden vocabulary
============================

I often have to read a lot of code from other people that is not exactly well written or easily understandable. I am working on several different projects; some open-source for fun & giggles and some closed-source for money & fame. I just noticed that the biggest problem in understanding other peoples code is not about things you could easily measure, like code quality in the sense of code formatting standards or the language that it is written in. Naming of constants and variables make all the difference for understanding the code others have written.

[![forbiddenvocabulary](/assets/images/forbiddenvocabulary.png)](http://fomori.org/blog/?attachment_id=873)I realized, that there are some words which should just be forbidden to use on their own. They are too broad or just don’t add any valuable information. I am also very sorry that these following examples contain PHP code, but this is where examples for doing things wrong are easily found. Most of the example code listings are not good practice in other senses as well, but that’s not what this post is about; It’s about the kind of readability which applies to all programming languages.

Shorter is not better
---------------------

Well, let’s start with an somewhat modified code snippet I had to work with:

```
function storeCampaignLifeStatsInDB($c){
    ...
    many lines of calculations
    ...
    $db->insert($c);
}
```

After reading what all the calculations are doing I already forgot what the heck $c was supposed to mean. To find out, I have to jump back and forth in the code, check its usages in other lines and hope that the function name is clear enough. Somehow I often see people trying to save characters to give their code more of a C feeling or something. Please, just don’t do it.

But how should the variable be called? Changing $c to $campaign certainly helps, but it is even better to give it a context of usage within the function, e.g. $campaign\_to\_store. Now it is clear that it’s the object I want to store in the database. The naming of course depends on the context and it doesn’t always make sense to name objects by their usage within a function. But if you can’t name your object so its usage within the function is clear, it might indicate that your function is doing too much and you should split it up.

JSON\_DATA\_OBJECT\_ARRAY
-------------------------

Okay, now something I see even more seasoned developers doing, can you spot the pattern?

```
$res = curl_exec($ch);
$obj = json_decode($res);
```

```
public function setData ($data) {
    if(!is_array($data)){
        $this->log[] = 'not a data array \n';
        return false;
    }
    $this->data = $data;
    return true;
}
```

```
$result = @file_get_contents($url, false, $context);            
$content = json_decode($result,true);
```

I am pretty sure you don’t have any idea what these snippets do or what the variables contain. Of course, theses are random code snippets and sometimes it might not be clear what some code is doing without any context. I will now give you an improved version of the code, by just changing the variable names.

```
$new_campaign_json = curl_exec($curl_options);
$new_campaign = json_decode($new_campaign_json);
```

```
public function setLoggingPayload ($debugValues) {
    if(!is_array($debugValues)){
        $this->log[] = 'not a data array \n';
        return false;
    }
    $this->debugValues = $debugValues;
    return true;
}
```

```
$facebook_events_json = @file_get_contents($facebook_graph_url, false, $request_options);            
$facebook_events = json_decode($facebook_events_json, true);
```

Now you immeadiately have a glimpse of what those lines do; I didn’t add any comments which you might forget to update later (wrong comments are worse than no comments) and also no additional lines to maintain. It’s all about naming things and not naming anything *data* or *object*. which bring us to…

List of forbidden vocabulary
----------------------------

Any of those words should not be used *on their own* in any code:

*array, data, json, list, object, result*

and of course any of their shorter cousins (*arr*, *obj*, *res*, etc…) and of course also their even shorter cousins (*a*, *b*, *c*, etc…)

Exceptions are of course, if you are really implementing a list etc. Feel free to add more examples in the comments.

Elements of style and usability
-------------------------------

Naming things correctly, and spending some thought on how to name things doesn’t only make your code more readable and maintainable, but also keeps you more focused on the task at hand. Writing code becomes more abstract each year. And with each level of abstraction we are getting further away from the machine and it’s limitations. We were once limited to 11 character filenames (ASCII only!), and 80 character terminals, but those times are long gone.

```
please_dont_get_me_wrong_and_overdo_it_ĐĦĸŁØ = "Hello World!"
```

This doesn’t mean that you should be too verbose when naming variables and you still might want to stick to ASCII names for your variables and try to make your lines not any longer than 80 or 99 characters depending on your coding standards. Using proper names you can completely avoid comments which describe what the code is doing; Instead just write comments *why* the code is doing something.

[![](/assets/images/71Jym5cRKEL._SL1077_.jpg)](http://amzn.com/020530902X)The higher the abstraction level, the more it all boils down [elementary principles of text composition.](https://en.wikipedia.org/wiki/The_Elements_of_Style) *Elements of style* by Strunk & White (S&W) explains in depth what words to use or avoid and how to compose a well written sentence within a properly structured paragraph. I think those rules apply to code in the same way. S&W argue, that a well written paragraph should make sense, even though you only read the first (topic sentence) and last sentence (conclusion) within it. This holds true for a function signature; The function name and the function parameter names form a topic sentence and the names of the return values (or variables) form the conclusion, which should describe what the function does entirely.

[![](/assets/images/51CjDVfvZwL.jpg)](http://www.sensible.com/dmmt.html)All this also leads basic usability principles. The user/coder should spend as little amount as necessary to understand your code. You should not expect a programmer to read the whole source code to understand a smaller part of it, just a user shouldn’t read all the text on a webpage to navigate to their goal. Or as Steve Krug puts it, [don’t make me think](http://www.sensible.com/dmmt.html).

If you haven’t read either of those books, I recommend them wholeheartedly.

 

  

	