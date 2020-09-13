//
//  TableViewController.swift
//  CraigslistApp
//
//  Created by Eric Nguyen on 9/11/20.
//  Copyright © 2020 Eric Nguyen. All rights reserved.
//

import UIKit


class SearchController: UITableViewController {
    
    var searches = [(id: Int, keywords: String, min_price: Int, max_price: Int)]()
    var id = 0
    var contact: Int?
    override func viewDidLoad() {
        super.viewDidLoad()

        APIHandler.getSearches{ [weak self] (searches) in
            self?.searches = searches
            self?.tableView.reloadData()
        }
        
           
    }
    func getId() -> Int {
        return id
    }
    // MARK: - Table view data source
   
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        id = searches[indexPath[1]].id
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return searches.count
        
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
   
        let cell = tableView.dequeueReusableCell(withIdentifier: "SearchItem", for: indexPath)

        cell.textLabel!.text = searches[indexPath[1]].keywords
        cell.detailTextLabel!.text = "Minimum Price: " + String(searches[indexPath[1]].min_price) + ", Maximum price: " + String(searches[indexPath[1]].max_price)
        
        return cell
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard let UrlController = segue.destination as? UrlController,
            let index = tableView.indexPathForSelectedRow?.row
            else{
                return
        }
        UrlController.contact = index
    }
    

}
