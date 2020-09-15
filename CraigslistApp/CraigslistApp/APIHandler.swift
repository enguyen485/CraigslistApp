//
//  File.swift
//  CraigslistApp
//
//  Created by Eric Nguyen on 9/10/20.
//  Copyright © 2020 Eric Nguyen. All rights reserved.
//

import Foundation
import Alamofire

class APIHandler {
    static func addURL(hyperlink: String, craigslist_id:Int, keywords: Int, date: String){
        print("Request Processing")
        let parameters: Parameters = ["hyperlink": hyperlink, "craigslist_id": craigslist_id, "keywords": keywords, "date": date]

        AF.request("http://127.0.0.1:5000/Url", method: .post, parameters: parameters).responseJSON { response in
            debugPrint(response)
        }
        
    }
    
    static func addDetector(keywords: String, min_price: Int, max_price: Int){
        print("Request Processing")
        let parameters: Parameters = ["keywords": keywords, "min_price": min_price, "max_price": max_price]

        AF.request("http://127.0.0.1:5000/Detector", method: .post, parameters: parameters).responseJSON { response in
            debugPrint(response)
        }
        
    }
    
    static func deleteUrl(id: Int){
        print("Request Processing")
        let parameters: Parameters = ["id": id]

        AF.request("http://127.0.0.1:5000/Url", method: .delete, parameters: parameters).responseJSON { response in
            debugPrint(response)
        }
        
    }
    
    static func getUrls(keywords: Int, completion: @escaping (_ urls: [(id: Int, hyperlink: String)])-> Void){
        print("Request Processing")
        let parameters: Parameters = ["keywords": keywords]
        AF.request("http://127.0.0.1:5000/Url", method: .get, parameters: parameters).responseJSON { response in
            if let json = response.value as? [String: AnyObject]{
                var returnUrl = [(id: Int, hyperlink: String )]()
                if let urls = json["urls"] as? [[String: AnyObject]]{
                    for url in urls{
                        returnUrl.append((id: url["id"] as! Int, hyperlink: url["hyperlink"] as! String))
                    }
                }
                completion(returnUrl)
            }
                
            
        }
       
    }
   
    static func getDetectors(completion: @escaping (_  detectors: [(id: Int, keywords: String, min_price: Int, max_price: Int)])-> Void){
           print("Request Processing")
           AF.request("http://127.0.0.1:5000/Detector", method: .get).responseJSON { response in
               if let json = response.value as? [String: AnyObject]{
                   var returnDetectors = [(id: Int, keywords: String, min_price: Int, max_price: Int)]()
                   if let  detectors = json["detectors"] as? [[String: AnyObject]]{
                       for  detector in  detectors{
                           returnDetectors.append((id:  detector["id"] as! Int, keywords: detector["keywords"] as! String, detector["min_price"] as! Int,  detector["max_price"] as! Int))
                       }
                   }
                   completion(returnDetectors)
               }
                   
               
           }
          
       }
}
