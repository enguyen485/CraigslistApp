//
//  ViewController.swift
//  CraigslistApp
//
//  Created by Eric Nguyen on 9/10/20.
//  Copyright © 2020 Eric Nguyen. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var FinishButton: UIButton!
    @IBOutlet weak var keywordsText: UITextField!
    @IBOutlet weak var minPrice: UITextField!
    @IBOutlet weak var maxPrice: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func onClick(_ sender: Any) {
        
        APIHandler.addDetector(keywords: keywordsText.text!, min_price: Int(minPrice.text!)!, max_price: Int(maxPrice.text!)!)
    }
    
}

