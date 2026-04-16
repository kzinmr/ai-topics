# Should you use a Lambda Monolith, aka Lambdalith, for your API?

Source: https://rehanvdm.com/blog/should-you-use-a-lambda-monolith-lambdalith-for-the-api/
Author: Rehan van der Merwe

## Core Thesis

モノリシックLambda関数("Lambdalith")は、APIルートごとに個別のLambda関数を作成するよりも優れている場合が多い。AWSの「ベストプラクティス」であるルート単位の関数分割は、過度に細分化された時期尚早な最適化であり、デプロイの複雑さを増すだけである。

## Lambdalithの利点

- 一元化されたロギング: 単一CloudWatchロググループ
- 高いROI: インフラのオーバーヘッド、デプロイの複雑さ、認知負荷の削減
- コードの再利用と一貫性: 重複排除、均一なエラーハンドリング
- 簡素化されたメンテナンス: 1つのコードベース

## Lambdalithの欠点

- ルート固有のメモリ/タイムアウト/IAM権限の制御が難しい
- パッケージサイズ肥大化によるコールドスタートの可能性

## 解決策

- 同じコードベースを複数のLambda関数にデプロイし、重いタスクには専用関数を使用
- ESBuildでツリーシェイキング
- JSONログ形式でCloudWatch Logs Insightsによるルートレベルのクエリを実現

## 重要な引用

> "爆発半径の境界は、従来のソフトウェアと同様にAPI/サービスレベルであるべきだ"
> "チーム規模が小さいうちはモノリスで十分。Conwayの法則に従い、チーム/プロジェクトの規模が必要になったらサービスを分割せよ"
