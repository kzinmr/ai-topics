---
title: "AI model achieves breakthrough in forecasting cyclones — Google DeepMind"
source: "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/"
author: "Google DeepMind"
date: "2026-05-XX"
date_ingested: "2026-08-10"
type: raw_article
tags:
  - trending
  - active-crawl
hn_url: "https://news.ycombinator.com/item?id=49220126"
hn_points: 441
---

# AI model achieves breakthrough in forecasting cyclones — Google DeepMind

**Source**: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/
**Author**: Google DeepMind
**Published**: 2026-05-XX
**HN Discussion**: https://news.ycombinator.com/item?id=49220126 (441 points)

{
    "reading_time": "[[read\u002Dtime]] min read"
  }

  

    
    

      

        
          

            

    

  

    

      

  

    

    

    

      
Breadcrumb

      

      
        

        
          

            Home
          

        
        

      
        

        
        

  

          
            

                Innovation & AI
            

          
        
        

      
        

        
        

  

          
            

                Models & research
            

          
        
        

      
        

        
        

  

          
            

                Google DeepMind
            

          
        
        

      
      
      
      

    

    

    

      

  

    

  

          

        
      

      
      

        

          
WeatherNext 2: Our most advanced weather forecasting model

          

            

              
              

                
                  
Nov 17, 2025

                
                
                  
|

                
                
                  

                
              

              

              

                

                

                

  

    

      

  

    

  

    
x.com

  

  

    

  

    
Facebook

  

  

    

  

    
LinkedIn

  

  

    

  

    
Mail

  

  

    

  

    
Copy link

  

  

    

  

    

  

              

            

            
            
              

                The new AI model delivers more efficient, more accurate and higher-resolution global weather predictions.
              

            
          

          

          
          

            

              
                

  
    
    

      

        
            
The WeatherNext team

            
              
            
        
      

    

  

              
            

            

              

              

                

                  Share
                

                

  

    

      

  

    

  

    
x.com

  

  

    

  

    
Facebook

  

  

    

  

    
LinkedIn

  

  

    

  

    
Mail

  

  

    

  

    
Copy link

  

  

    

  

    

  

              

            

          

          

        

      

    

    
    

      
        

  
    

      

        

          

        

      

      
    

  

  class ProgressiveImage {
    EVENTS = {
      TRANSITION_END: 'transitionend',
    };

    CSS_CLASSES = {
      BLUR: 'uni-progressive-image--blur',
      NO_BLUR: 'uni-progressive-image--no-blur',
    };

    init(el) {
      this.el = el;
      this._events();
      this._upgradeImage();
    }

    _upgradeImage() {
      // For gif format images we don't include data-srcset and data-sizes
      // We can safely remove the blur filter.
      if (!this.el.dataset.srcset || !this.el.dataset.sizes) {
        this.el.classList.add(this.CSS_CLASSES.NO_BLUR);

        return;
      }

      this.el.setAttribute('srcset', this.el.dataset.srcset);
      this.el.setAttribute('sizes', this.el.dataset.sizes);
      requestAnimationFrame(() => {
        this.el.classList.add(this.CSS_CLASSES.NO_BLUR);
      });
    }

    _events() {
      // Once the transition completes is safe to clean some attributes
      this.el.addEventListener(this.EVENTS.TRANSITION_END, () => {
        this.el.classList.remove(this.CSS_CLASSES.BLUR, this.CSS_CLASSES.NO_BLUR);
        this.el.removeAttribute('data-srcset');
        this.el.removeAttribute('data-sizes');
      });
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('[data-component="uni-progressive-image"]');
    images.forEach((el) => {
      el.setAttribute('data-component-initialized', true);
      new ProgressiveImage().init(el);
    });
  });

      
    

  

    

      

        
        
          
            

  

    

      

        

  

      

      

        Read AI-generated summary
        

          

  

        

      

    

    

      

        
          

            

              
Google's WeatherNext 2 is here, giving you faster and more detailed weather forecasts using AI. This new model predicts hundreds of weather scenarios in under a minute. You can now access WeatherNext 2 forecast data in Earth Engine and BigQuery, or join the early access program on Google Cloud's Vertex AI.

            

            

              Summaries were generated by Google AI. Generative AI is experimental.
            

          

        
          

            

              

"WeatherNext 2" is Google's new AI weather model, forecasting faster and more efficiently than ever before.

WeatherNext 2 generates hundreds of possible weather scenarios in under a minute, using just one TPU.

This model surpasses the previous WeatherNext model on 99.9% of variables and lead times.

WeatherNext 2 data is now available in Earth Engine and BigQuery, with Vertex AI early access.

WeatherNext 2 upgrades weather forecasts in Search, Gemini, Pixel Weather, Maps Platform, and Maps.

            

            

              Summaries were generated by Google AI. Generative AI is experimental.
            

          

        
          

            

              
Google made a super smart weather tool called WeatherNext 2. It uses computers to guess the weather faster and better than before. It can even show many different weather possibilities. Now, people can use it to help make important choices about the weather.

            

            

              Summaries were generated by Google AI. Generative AI is experimental.
            

          

        

        
        

          

            Explore other styles:
          

          

            
            

              

                
                  

  

                
                

                  General summary
                

              

            

            
            

              

                
                  

  

                
                

                  Bullet points
                

              

            

            
            

              

                
                  

  

                
                

                  Basic explainer
                

              

            

            
          

        

        
      

    

  

          
        
      

    

    
    

      
        
        
        

          
          

  
    

  

    

The weather affects important decisions we make everyday — from global supply chains and flight paths to your daily commute. In recent years, artificial intelligence (AI) has dramatically enhanced what’s possible in weather forecasting and the ways in which we can use it.

Today, Google DeepMind and Google Research are introducing 
WeatherNext 2
, our most advanced and efficient forecasting model. WeatherNext 2 can generate forecasts 8x faster and with resolution up to 1-hour. This breakthrough is enabled by a new model that can provide hundreds of possible scenarios. Using this technology, we’ve supported weather agencies in making decisions based on a range of scenarios through our 
experimental cyclone predictions
.

We're now taking our research out of the lab and putting it into the hands of users. WeatherNext 2's forecast data is now available in 
Earth Engine
 and 
BigQuery
. We’re also launching an 
early access program
 on Google Cloud’s Vertex AI platform for custom model inference.

By incorporating WeatherNext technology, we’ve now upgraded weather forecasts in Search, Gemini, Pixel Weather and Google Maps Platform’s 
Weather API
. In the coming weeks, it will also help power weather information in Google Maps.

  

  

  
    
  
    

  {
    "@context": "https://schema.org/",
    "@type": "VideoObject",
    "name": "WeatherNext 2: Our most advanced weather forecasting model",
    "description": "WeatherNext demo video",
    "thumbnailUrl": "https://i.ytimg.com/vi_webp/YQwqoEm_xis/maxresdefault.webp",
    "uploadDate": "2025-11-17T15:00:00+00:00",
    "contentUrl": "https://www.youtube.com/watch?v=YQwqoEm_xis",
    "embedUrl": "https://www.youtube.com/embed/YQwqoEm_xis"
  }

  

  

  
    

  

    

Predicting more possible scenarios

  

  

  
    

  
  
  
  
  

  {
    "play_video": "Play video",
    "pause_video": "Pause video"
  }

  {
    "play_video": "Play video",
    "pause_video": "Pause video",
    "mute": "Click to mute audio",
    "unmute": "Click to unmute audio",
    "enable_cc": "Enable Closed captions",
    "disable_cc": "Disable Closed captions",
    "disable_ad": "Disable audio description",
    "enable_ad": "Enable audio description",
    "video_progress": "Video progress",
    "aria_value_text": "elapsed time: [[elapsedTime]], total time: [[totalTime]]"
  }

  

    
      

        

From a single input, we use independently trained neural networks and inject noise in function space to create coherent variability in weather forecast predictions.

      

    

    
      

        

      

    
  

  

  
    

  

    

Weather predictions need to capture the full range of possibilities — including worst case scenarios, which are the most important to plan for.

WeatherNext 2 can predict hundreds of possible weather outcomes from a single starting point. Each prediction takes less than a minute on a single TPU; it would take hours on a supercomputer using physics-based models.

Our model is also highly skillful and capable of higher-resolution predictions, down to the hour. Overall, WeatherNext 2 surpasses our previous state-of-the-art WeatherNext model on 99.9% of variables (e.g. temperature, wind, humidity) and lead times (0-15 days), enabling more useful and accurate forecasts.

This improved performance is enabled by a new AI modelling approach called a 
Functional Generative Network
 (FGN), which injects ‘noise’ directly into the model architecture so the forecasts it generates remain physically realistic and interconnected.

This approach is particularly useful for predicting what meteorologists refer to as “marginals” and “joints.” Marginals are individual, standalone weather elements: the precise temperature at a specific location, the wind speed at a certain altitude or the humidity. What's novel about our approach is that the model is only trained on these marginals. Yet, from that training, it learns to skillfully forecast 'joints' — large, complex, interconnected systems that depend on how all those individual pieces fit together. This 'joint' forecasting is required for our most useful predictions, such as identifying entire regions affected by high heat, or expected power output across a wind farm.

  

  

  
    

  
  
  
  
  

  {
    "play_video": "Play video",
    "pause_video": "Pause video"
  }

  {
    "play_video": "Play video",
    "pause_video": "Pause video",
    "mute": "Click to mute audio",
    "unmute": "Click to unmute audio",
    "enable_cc": "Enable Closed captions",
    "disable_cc": "Disable Closed captions",
    "disable_ad": "Disable audio description",
    "enable_ad": "Enable audio description",
    "video_progress": "Video progress",
    "aria_value_text": "elapsed time: [[elapsedTime]], total time: [[totalTime]]"
  }

  

    
      

        

Continuous Ranked Probability Score (CRPS) comparing WeatherNext 2 to WeatherNext Gen

      

    

    
      

        

      

    
  

  

  
    

  

    

From research to reality

With WeatherNext 2, we're translating cutting edge research into high-impact applications. We’re committed to advancing the state of the art of this technology and making our latest tools available to the global community.

  

  

  
    

  {
    "play_video": "Play video",
    "pause_video": "Pause video"
  }

  {
    "play_video": "Play video",
    "pause_video": "Pause video",
    "mute": "Click to mute audio",
    "unmute": "Click to unmute audio",
    "enable_cc": "Enable Closed captions",
    "disable_cc": "Disable Closed captions",
    "disable_ad": "Disable audio description",
    "enable_ad": "Enable audio description",
    "video_progress": "Video progress",
    "aria_value_text": "elapsed time: [[elapsedTime]], total time: [[totalTime]]"
  }

  

    

    
  

  

  
    

  

    

Looking ahead, we’re actively researching capabilities to improve our models, including integrating new data sources, and expanding access even further. By providing powerful tools and open data, we hope to accelerate scientific discovery and empower a global ecosystem of researchers, developers and businesses to make decisions on today’s most complex problems and build for the future.

To learn more about geospatial platforms and AI work at Google, check out 
Google Earth
, 
Earth Engine
, 
AlphaEarth Foundations
, and 
Earth AI
.

Learn more about WeatherNext 2

Read our paper

WeatherNext developer documentation

Explore the 
Earth Engine Data Catalog

Query forecast data in 
BigQuery

Sign up to the 
early access program
 for Cloud Vertex AI

  

  

  
    

  {
    "see_more": "See more"
  }

  

    

      

        
          
Google DeepMind Blog

        

        

          GenCast predicts weather and the risks of extreme conditions
        

        
          
New AI model advances the prediction of weather uncertainties and risks, delivering faster, more accurate forecasts up to 15 days ahead.

        

        
          

            

              See more
            

          

        
      

      

        
          
            
            
            

            

          
        
      

    

  

  

  
    

  {
    "see_more": "See more"
  }

  

    

      

        
          
Google DeepMind Blog

        

        

          GraphCast
        

        
          
An AI model for faster and more accurate global weather forecasting.

        

        
          

            

              See more
            

          

        
      

      

        
          
            
            
            

            

          
        
      

    

  

  

          
          

          
            

  

    

      
POSTED IN:

    

    

      

        
        
          
          
          
            

              

  

    Google DeepMind
  

            

          
        

        
          
          
          
            

              

  

    AI Products
  

            

          
        
          
          
          
            

              

  

    Google Research

## HN Discussion (441 points, 25 comments)

**bhavansig** (None pts): From the tagline in the article: "WeatherNext enables accurate cyclone forecasts that can give an extra day of warning. Now we are open sourcing the model."

**jen729w** (None pts): I just discovered typhoon/cyclone predictions and they're insane. I get mine via https://zoom.earth (whose iPhone app is terrific). Here's a selection from Typhoon Dolphin, currently sitting off the east coast of China. Dolphin continues its slow, trochoidal Z motion, generally heading westward deeper into the East China Sea. Over the past 12 hours, the system completed another cyclonic loop and has decelerated, exhibiting continued meandering prior to establishing a sustained westward track. The erratic motion witnessed over the past two days is attributable to a weak steering environment produced by a break in the subtropical ridge 2 over Korea, combined with the dynamics where the inner core is cocooned within a much larger parent circulation. While the general steering pattern is weak, a mesoscale deep-layer ridge is seen building over southern Japan. https://zoom.earth/storms/dolphin-2026/ Here's Chan-hom, which threatens to make my birthday a windy day here in northern Japan. Intensity guidance is in good agreement overall. However, the JTWC forecast is placed lower than all the guidance save for Google DeepMind over the next 36 hours, before joining the consensus envelope (which peaks at 95 km/h (50 knots) at 60 hours) through the remainder of the forecast. https://zoom.earth/storms/chan-hom-2026/

**moktonar** (None pts): They should try to forecast earthquakes, that would really be a breakthrough If anything better than random comes out

**pingou** (None pts): It seems especially useful for cargo ships, with better predictions they could save some fuel and be safer.

**fcanesin** (None pts): Maybe was this that was the last drop for Sundar. Demis: "I have a new amazing breakthrough" Sundar: "Great! We really need a answer to Sol and Fable" Demis: "They are completely owned in typhoon forecasting"

**snake_doc** (None pts): > We can now generate a single 15-day forecast in less than a minute on a TPU, empowering forecasters to quickly evaluate the probability distribution of potentially devastating tail-risks. Crazy

**dgellow** (None pts): This is really cool, please more of this from the AI folks! That’s way more impactful and interesting than another coding agent

**_alternator_** (None pts): Accurate weather forecasting has been one of the major achievements of the 20th and 21st century. Computing power is a central piece of this story, but it's also important to remember that the government infrastructure in place to collect ground-truth current weather data is utterly critical to these model's successes. From launching weather balloons to running global weather-monitoring satellites, the scientists and systems at NOAA/NWS (and in this case, the UK counterparts) provide critical expertise and data. I say this because it seems that earlier announcements where industrial deep neural nets "outperformed NOAA" likely encouraged the slash-and-burn Trump administration in its gutting of critical activities and centers of expertise at NOAA. The impression that industry can predict weather better than the government agencies totally misses that the industrial models utterly rely on government data for inputs. In fact, almost all weather reports you see---weather.com, TV, etc.---are just lightly repackaged products that NOAA provides for free on weather.gov (which you can access for free without ads).

**tcumulus** (None pts): Everything in AI seems to be focused on LLMs lately. But in my opinion, powerful problem-specific models like this are even more interesting. The SOTA AI models used in weather forecasting are already outperforming the classic NWP models while being orders of magnitude more efficient (inference). Most are based on multi scale (hierarchical) Graph Neural Networks, an architecture which is not often talked about. The original Graphcast paper is worth a read if you think this is interesting: https://arxiv.org/abs/2212.12794

**throw310822** (None pts): Next step: steering them. (As in Permutation City's "Operation Butterfly".)

**purplemoonx** (None pts): Predicting big weather events is not that hard even with 50 year old technology. What's hard is predicting details, like exactly where it will rain, what the slope of the beach is today (many people don't even know this changes drastically daily and why it is important), wave height, ocean depth today where people swim, water temperature, shorebreak, and knowing with certainty when rain becomes ice/sleet/snow and what routes will be affected, accurate wind speed, accurate temperature throughout different parts of the region, and what the weather next week will be. We can't do any of those things with conventional equipment, but we can with training data and algorithms. So I'm very excited about the role of algorithmic prediction in weather, but not for the kind we already know how to forecast (without AI) but being able to glean useful insights that matter to people who live, work and play in the weather.

**pbronez** (None pts): Cool how they integrated both huge machine-scale data and smaller human-curated data for this project. > The model was co-trained on two distinct data modalities: global weather dynamics and expert-curated historical cyclone observations. By training end-to-end on nearly 20 terabytes of global atmospheric data and the historical IBTrACS database spanning nearly 5,000 historical storms, the model learns complex atmospheric patterns and how to model extreme weather.

**noduerme** (None pts): Ask Gemini why google maps doesn't have a weather layer. Its justifications are defensive rubbish, even for Gemini.

**kashifr** (None pts): Check out my pytorch reproduction of the paper here for those interested: https://github.com/NVIDIA/physicsnemo/pull/1660

**HardCodedBias** (None pts): And this is why GDM has to go. It's crazy that when Google is struggling so badly that efforts like this that have no path to revenue at all were funded. GDM management really thought that they were some kind of charity. UNREAL.


